import math

def calculate_gravity(distance, time):
    gravity = 2 * distance / math.pow(time, 2)
    return gravity

def calculate_percentage_error(calculated_g, actual_g):
    percentage_error = abs((calculated_g - actual_g) / actual_g) * 100
    return percentage_error

def print_ascii_art_if_error_is_low():
    ascii_art = """
Suddenly, a wild cat appears.

(_＼ヽ
 ＼＼ .Λ＿Λ.
 ＼(　ˇωˇ)　
 >　⌒ヽ
 / へ＼
 / /　＼＼
 ﾚ　ノ ヽ_つ
 /　/
 /　/|
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| | ) /
`ノ ) Lﾉ
(_／
"""
    print(ascii_art)

def print_mermaid_ascii_art_if_error_is_high():
    mermaid_art = """
                         .-""-.
                        (___/\ \
        ,                 (|^ ^ ) )
       /(                _)_\=_/  (
 ,..__/ `\          ____(_/_ ` \   )
  `\    _/        _/---._/(_)_  `\ (
     '--\ `-.__..-'    /.    (_), |  )
       `._        ___\_____.'_| |__/
           `~----"`   `-.........'
"""
    print(mermaid_art)

def print_ghost_ascii_art_if_error_is_very_high():
    ghost_art = """
 .-._                                                   _,-,
  `._`-._                                           _,-'_,'
     `._ `-._                                   _,-' _,'
        `._  `-._        __.-----.__        _,-'  _,'
           `._   `#==="""           """===#'   _,'
              `._/)  ._               _.  (\_,'
               )*'     **.__     __.**     '*( 
               #  .==..__  ""   ""  __..==,  # 
                #   `"._(_).       .(_)_."'   #
"""
    print(ghost_art)

calculated_g = float(input("Enter your calculated g value: "))
actual_g = 9.81

percentage_error = calculate_percentage_error(calculated_g, actual_g)

if percentage_error < 20:
    print_ascii_art_if_error_is_low()
elif percentage_error >= 20 and percentage_error < 75:
    print_mermaid_ascii_art_if_error_is_high()
else:
    print_ghost_ascii_art_if_error_is_very_high()

