# -*- coding: utf-8 -*-
import random
import time
import csv
import json
import os
from datetime import datetime

# ── Colors ───────────────────────────────────────────────────────────────────
G  = '\033[92m'
R  = '\033[91m'
Y  = '\033[93m'
C  = '\033[96m'
B  = '\033[1m'
DM = '\033[2m'
X  = '\033[0m'

# ── Trachtenberg method hints ─────────────────────────────────────────────────
HINTS = {
    2:  "Удвойте каждую цифру числа",
    3:  "Удвойте предыдущую цифру + текущая",
    4:  "Применить ×2 дважды",
    5:  "Разделить на 2, умножить на 10",
    6:  "Текущая + ½ предыдущей (+5 если предыдущая нечётная)",
    7:  "Удвоить текущую + ½ следующей (+5 если следующая нечётная)",
    8:  "(10 − правая), затем (9 − цифра + перенос)",
    9:  "(10 − правая цифра), затем (9 − цифра)",
    11: "Первая и последняя цифры те же; средние = сумма соседей",
    12: "Удвоить текущую цифру + правый сосед",
}

# ── Question generators ───────────────────────────────────────────────────────
def gen_mult(n, mult, lo=101, hi=10000):
    return [(random.randrange(lo, hi), mult) for _ in range(n)]

def gen_two_x_two(n):
    return [(random.randrange(10, 100), random.randrange(10, 100)) for _ in range(n)]

def gen_multi(n):
    return [(random.randrange(100, 1000), random.randrange(10, 100)) for _ in range(n)]

def gen_any_len(n):
    return [(random.randrange(100, 99000), random.randrange(100, 999)) for _ in range(n)]

SQ_END5  = [15, 25, 35, 45, 55, 65, 75, 85, 95]
SQ_START5 = [51, 52, 53, 54, 56, 57, 58, 59]

def gen_sq_end5():
    arr = SQ_END5.copy()
    random.shuffle(arr)
    return [(x, x) for x in arr]

def gen_sq_start5():
    arr = SQ_START5.copy()
    random.shuffle(arr)
    return [(x, x) for x in arr]

def gen_sq(n):
    return [(x, x) for x in [random.randrange(10, 100) for _ in range(n)]]

# ── Category definitions ──────────────────────────────────────────────────────
CATEGORIES = [
    {'name': 'Умножение на 11',         'fn': lambda: gen_mult(5, 11),   'count': 5,  'hint': 11,   'default': True},
    {'name': 'Умножение на 12',         'fn': lambda: gen_mult(5, 12),   'count': 5,  'hint': 12,   'default': True},
    {'name': 'Умножение на 9',          'fn': lambda: gen_mult(5, 9),    'count': 5,  'hint': 9,    'default': True},
    {'name': 'Умножение на 8',          'fn': lambda: gen_mult(5, 8),    'count': 5,  'hint': 8,    'default': True},
    {'name': 'Умножение на 7',          'fn': lambda: gen_mult(5, 7),    'count': 5,  'hint': 7,    'default': False},
    {'name': 'Умножение на 6',          'fn': lambda: gen_mult(5, 6),    'count': 5,  'hint': 6,    'default': False},
    {'name': 'Умножение на 5',          'fn': lambda: gen_mult(5, 5),    'count': 5,  'hint': 5,    'default': False},
    {'name': 'Умножение на 4',          'fn': lambda: gen_mult(5, 4),    'count': 5,  'hint': 4,    'default': False},
    {'name': 'Умножение на 3',          'fn': lambda: gen_mult(5, 3),    'count': 5,  'hint': 3,    'default': False},
    {'name': 'Умножение на 2',          'fn': lambda: gen_mult(5, 2),    'count': 5,  'hint': 2,    'default': False},
    {'name': 'Двузначное × двузначное', 'fn': lambda: gen_two_x_two(5), 'count': 5,  'hint': None, 'default': True},
    {'name': 'Многозначные множимые',   'fn': lambda: gen_multi(5),      'count': 5,  'hint': None, 'default': True},
    {'name': 'Умножение любой длины',   'fn': lambda: gen_any_len(5),    'count': 5,  'hint': None, 'default': True},
    {'name': 'Квадрат (оканч. на 5)',   'fn': gen_sq_end5,               'count': len(SQ_END5),    'hint': None, 'default': True},
    {'name': 'Квадрат (начин. с 5)',    'fn': gen_sq_start5,             'count': len(SQ_START5),  'hint': None, 'default': True},
    {'name': 'Возведение в квадрат',    'fn': lambda: gen_sq(6),         'count': 6,  'hint': None, 'default': True},
]

RECORDS_FILE = 'records.json'
LOG_FILE = 'log.csv'

# ── Records & Log ─────────────────────────────────────────────────────────────
def load_records():
    if os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, encoding='utf-8') as f:
            return json.load(f)
    return {'best_pct': 0.0, 'best_avg_sec': None, 'sessions': 0}

def save_records(rec):
    with open(RECORDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(rec, f, indent=2, ensure_ascii=False)

def append_log(correct, wrong, pct, avg_sec, cat_names):
    existed = os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        if not existed:
            w.writerow(['date', 'correct', 'wrong', 'pct', 'avg_sec', 'categories'])
        w.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M'),
            correct, wrong,
            f'{pct:.1f}',
            f'{avg_sec:.2f}' if avg_sec is not None else '',
            '|'.join(cat_names),
        ])

# ── Display helpers ───────────────────────────────────────────────────────────
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_progress(done, total, correct, wrong):
    W = 24
    filled = int(W * done / total) if total else 0
    bar = f"{C}{'█' * filled}{DM}{'░' * (W - filled)}{X}"
    print(f"  [{bar}] {DM}{done}/{total}{X}  {G}✓ {correct}{X}  {R}✗ {wrong}{X}")

def sep(width=44):
    print(f"{DM}{'─' * width}{X}")

# ── Single question ───────────────────────────────────────────────────────────
def ask_question(a, b, q_num, q_total, correct, wrong, cat_name, show_hints, hint_key):
    print()
    print(f"  {B}{cat_name}{X}  {DM}({q_num}/{q_total}){X}")
    sep()
    draw_progress(q_num - 1, q_total, correct, wrong)
    print()
    print(f"  {B}{a} × {b} = ?{X}")
    print()

    t0 = time.time()
    while True:
        try:
            ans = int(input(f"  {Y}>{X} "))
            elapsed = time.time() - t0
            break
        except ValueError:
            print(f"  {R}Введите целое число!{X}")

    correct_ans = a * b
    if ans == correct_ans:
        print(f"\n  {G}{B}✓ Верно!{X}  {DM}({elapsed:.1f} сек){X}")
        return True, elapsed
    else:
        print(f"\n  {R}{B}✗ Неверно.{X}  Правильный ответ: {B}{correct_ans}{X}  {DM}({elapsed:.1f} сек){X}")
        if show_hints and hint_key and hint_key in HINTS:
            print(f"  {C}{DM}Подсказка: {HINTS[hint_key]}{X}")
        return False, elapsed

# ── Run one category ──────────────────────────────────────────────────────────
def run_category(cat, show_hints):
    questions = cat['fn']()
    n = len(questions)
    cat_correct = 0
    cat_wrong = 0
    times = []
    interrupted = False

    try:
        for i, (a, b) in enumerate(questions):
            clear_screen()
            print(f"\n{B}{C}  ══ {cat['name'].upper()} ══{X}\n")

            ok, elapsed = ask_question(
                a, b,
                q_num=i + 1,
                q_total=n,
                correct=cat_correct,
                wrong=cat_wrong,
                cat_name=cat['name'],
                show_hints=show_hints,
                hint_key=cat.get('hint'),
            )
            times.append(elapsed)
            if ok:
                cat_correct += 1
            else:
                cat_wrong += 1

            if i < n - 1:
                input(f"\n  {DM}Enter → следующий вопрос...{X}")
    except (KeyboardInterrupt, EOFError):
        interrupted = True

    if not interrupted and (cat_correct + cat_wrong) > 0:
        cat_pct = 100 * cat_correct / (cat_correct + cat_wrong)
        print(f"\n  {DM}─── Итог раздела: {G}{cat_correct}{X}/{n}  ({cat_pct:.0f}%){DM} ───{X}")
        try:
            input(f"\n  {DM}Enter → продолжить...{X}")
        except (KeyboardInterrupt, EOFError):
            interrupted = True

    return cat_correct, cat_wrong, times, interrupted

# ── Category selection menu ───────────────────────────────────────────────────
def select_categories():
    selected = [cat['default'] for cat in CATEGORIES]
    show_hints = True

    while True:
        clear_screen()
        print(f"\n{B}{C}╔════════════════════════════════════╗{X}")
        print(f"{B}{C}║    СИСТЕМА ТРАХТЕНБЕРГА  v2.0      ║{X}")
        print(f"{B}{C}╚════════════════════════════════════╝{X}\n")

        for i, cat in enumerate(CATEGORIES):
            mark = f"{G}[✓]{X}" if selected[i] else f"{DM}[ ]{X}"
            tag = f" {Y}+{X}" if not cat['default'] else ''
            print(f"  {DM}{i+1:2d}.{X} {mark} {cat['name']}{tag}")

        hint_mark = f"{G}[✓]{X}" if show_hints else f"{DM}[ ]{X}"
        count = sum(selected)
        total_q = sum(CATEGORIES[i]['count'] for i in range(len(CATEGORIES)) if selected[i])

        print(f"\n   H.  {hint_mark} Подсказки (метод Трахтенберга)\n")
        sep()
        print(f"  {DM}[A]{X} Все  {DM}[N]{X} Снять  {DM}[S]{X} {G}{B}Начать{X}")
        print(f"  {DM}Выбрано: {count} кат., ~{total_q} вопросов{X}")

        cmd = input(f"\n  {Y}>{X} ").strip().lower()

        if cmd == 's':
            if count == 0:
                print(f"  {R}Выберите хотя бы одну категорию!{X}")
                time.sleep(1)
            else:
                break
        elif cmd == 'a':
            selected = [True] * len(CATEGORIES)
        elif cmd == 'n':
            selected = [False] * len(CATEGORIES)
        elif cmd == 'h':
            show_hints = not show_hints
        else:
            try:
                idx = int(cmd) - 1
                if 0 <= idx < len(CATEGORIES):
                    selected[idx] = not selected[idx]
            except ValueError:
                pass

    return [CATEGORIES[i] for i in range(len(CATEGORIES)) if selected[i]], show_hints

# ── Final results ─────────────────────────────────────────────────────────────
def show_results(correct, wrong, all_times, chosen_cats, per_cat, interrupted=False):
    total = correct + wrong
    pct = 100 * correct / total if total else 0
    avg_sec = sum(all_times) / len(all_times) if all_times else None

    rec = load_records()
    rec['sessions'] += 1
    new_pct_record = not interrupted and total > 0 and pct > rec['best_pct']
    new_time_record = (not interrupted and avg_sec is not None and
                       (rec['best_avg_sec'] is None or avg_sec < rec['best_avg_sec']))
    if new_pct_record:
        rec['best_pct'] = pct
    if new_time_record:
        rec['best_avg_sec'] = avg_sec
    save_records(rec)

    if total > 0:
        append_log(correct, wrong, pct, avg_sec, [c['name'] for c in chosen_cats])

    clear_screen()
    title = "ПРЕРВАНО" if interrupted else "РЕЗУЛЬТАТЫ"
    print(f"\n{B}{C}╔════════════════════════════════════╗{X}")
    print(f"{B}{C}║{title:^36s}║{X}")
    print(f"{B}{C}╚════════════════════════════════════╝{X}\n")

    if total == 0:
        print(f"  {DM}Ни одного вопроса не пройдено.{X}\n")
        sep()
        input(f"\n  {DM}Enter для выхода...{X}")
        return

    print(f"  Правильных:    {G}{B}{correct}{X} / {total}")
    print(f"  Неправильных:  {R}{B}{wrong}{X} / {total}")

    pct_color = G if pct >= 90 else (Y if pct >= 70 else R)
    pct_record = f"  {Y}{B}★ Новый рекорд!{X}" if new_pct_record else ''
    print(f"\n  Результат: {pct_color}{B}{pct:.1f}%{X}{pct_record}")

    if avg_sec is not None:
        time_record = f"  {Y}{B}★ Лучшее время!{X}" if new_time_record else ''
        print(f"  Среднее время: {B}{avg_sec:.1f} сек{X}{time_record}")

    if per_cat:
        print(f"\n  {B}По категориям:{X}")
        sep()
        for name, c_corr, c_total, c_avg in per_cat:
            if c_total == 0:
                continue
            cp = 100 * c_corr / c_total
            cp_color = G if cp >= 90 else (Y if cp >= 70 else R)
            time_str = f"{c_avg:.1f}s" if c_avg is not None else '—'
            print(f"  {cp_color}{cp:5.1f}%{X}  {DM}{c_corr}/{c_total}{X}  {DM}avg {time_str:>6s}{X}  {name}")

    sessions = rec['sessions']
    best_pct = rec['best_pct']
    best_time = f"{rec['best_avg_sec']:.1f} сек" if rec['best_avg_sec'] is not None else '—'
    print(f"\n  {DM}Сессий: {sessions}  |  Рекорд: {best_pct:.1f}%  |  Лучшее время: {best_time}{X}")
    print(f"  {DM}Лог записан в {LOG_FILE}{X}\n")
    sep()
    input(f"\n  {DM}Enter для выхода...{X}")

# ── Entry point ───────────────────────────────────────────────────────────────
def main():
    chosen_cats, show_hints = select_categories()

    all_correct = 0
    all_wrong = 0
    all_times = []
    per_cat = []
    interrupted = False

    for cat in chosen_cats:
        c, w, times, was_interrupted = run_category(cat, show_hints)
        all_correct += c
        all_wrong += w
        all_times.extend(times)
        if (c + w) > 0:
            avg = sum(times) / len(times) if times else None
            per_cat.append((cat['name'], c, c + w, avg))
        if was_interrupted:
            interrupted = True
            break

    show_results(all_correct, all_wrong, all_times, chosen_cats, per_cat, interrupted)

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{Y}Выход.{X}")
