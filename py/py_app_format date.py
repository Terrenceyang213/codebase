import datetime
#%% 日期格式
dt = datetime.datetime(2010, 7, 4, 12, 15, 58)
'{:%Y-%m-%d %H:%M:%S}'.format(dt)
#out[]: '2010-07-04 12:15:58'

dt = datetime.date.today()
strdate = "{year:04d}-{month:02d}-{day:02d}".format(year=dt.year, month=dt.month, day=dt.day)
strdate = "{:%Y-%m-%d}".format(dt)
f"{dt.year:04d}-{dt.month:02d}-{dt.day:02d}" #字符串字面值插值
#out[]: '2021-04-15'
#out[]: '2021-04-15'
#out[]: '2021-04-15'

################################
# %a 当地工作日的缩写。
# Sun, Mon, ..., Sat (en_US);
# So, Mo, ..., Sa (de_DE)



################################
# %A 本地化的星期中每日的完整名称。
# Sunday, Monday, ..., Saturday (en_US);
# Sonntag, Montag, ..., Samstag (de_DE)



################################
# %w 以十进制数显示的工作日，其中0表示星期日，6表示星期六。
# 0, 1, ..., 6



################################
# %d 补零后，以十进制数显示的月份中的一天。
# 01, 02, ..., 31



################################
# %b 当地月份的缩写。
# Jan, Feb, ..., Dec (en_US);
#Jan, Feb, ..., Dez (de_DE)



################################
# %B 本地化的月份全名。
# January, February, ..., December (en_US);
# Januar, Februar, ..., Dezember (de_DE)



################################
# %m 补零后，以十进制数显示的月份。
# 01, 02, ..., 12



################################
# %y 补零后，以十进制数表示的，不带世纪的年份。
# 00, 01, ..., 99



################################
# %Y 十进制数表示的带世纪的年份。
# 0001, 0002, ..., 2013, 2014, ..., 9998, 9999



################################
# %H 以补零后的十进制数表示的小时（24 小时制）。
# 00, 01, ..., 23



################################
# %I 以补零后的十进制数表示的小时（12 小时制）。
# 01, 02, ..., 12



################################
# %p 本地化的 AM 或 PM 。
# AM, PM (en_US);
# am, pm (de_DE)



################################
# %M 补零后，以十进制数显示的分钟。
# 00, 01, ..., 59



################################
# %S 补零后，以十进制数显示的秒。
# 00, 01, ..., 59



################################
# %f 以十进制数表示的微秒，在左侧补零。
# 000000, 000001, ..., 999999


################################
# %z UTC 偏移量，格式为 ±HHMM[SS[.ffffff]] （如果是简单型对象则为空字符串）。
# (空), +0000, -0400, +1030, +063415, -030712.345216


################################
# %Z 时区名称（如果对象为简单型则为空字符串）。
# (空), UTC, GMT



################################
# %j 以补零后的十进制数表示的一年中的日序号。
# 001, 002, ..., 366



################################
# %U 以补零后的十进制数表示的一年中的周序号（星期日作为每周的第一天）。 在新的一年中第一个星期日之前的所有日子都被视为是在第 0 周。
# 00, 01, ..., 53



################################
# %W 以十进制数表示的一年中的周序号（星期一作为每周的第一天）。 在新的一年中第一个第期一之前的所有日子都被视为是在第 0 周。
# 00, 01, ..., 53



################################
# %c 本地化的适当日期和时间表示。
# Tue Aug 16 21:30:00 1988 (en_US);
# Di 16 Aug 21:30:00 1988 (de_DE)



################################
# %x 本地化的适当日期表示。
# 08/16/88 (None);
# 08/16/1988 (en_US);
# 16.08.1988 (de_DE)



################################
# %X 本地化的适当时间表示。
# 21:30:00 (en_US);
# 21:30:00 (de_DE)



################################
# '%%' 字面的 '%' 字符。
# %


dt #datetime.datetime(2021, 4, 15, 23, 59, 18, 395180)
'{:%Y-%m-%d-%A-%w-%U}'.format(dt)
# Out[20]: '2021-04-15-Thursday-4-15'