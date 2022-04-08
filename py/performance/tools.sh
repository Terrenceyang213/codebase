python -m cProfile -s cumulative julia1_nopil.py
# julia1_nopil.py必须在__main__里面调用想要测试的函数
# Length of x: 1000
# Total elements: 1000000
# calculate_z_serial_purepython took 10.134655475616455 seconds
#          36221995 function calls in 10.721 seconds

#    Ordered by: cumulative time

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   10.721   10.721 {built-in method builtins.exec}
#         1    0.029    0.029   10.721   10.721 julia1_nopil.py:1(<module>)
#         1    0.445    0.445   10.693   10.693 julia1_nopil.py:23(calc_pure_python)
#         1    7.098    7.098   10.135   10.135 julia1_nopil.py:9(calculate_z_serial_purepython)
#  34219980    3.037    0.000    3.037    0.000 {built-in method builtins.abs}
#   2002000    0.105    0.000    0.105    0.000 {method 'append' of 'list' objects}
#         1    0.008    0.008    0.008    0.008 {built-in method builtins.sum}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         2    0.000    0.000    0.000    0.000 {built-in method time.time}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


python -m cProfile -o profile.stats julia1.py