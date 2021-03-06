    char： char 类型占用 1 字节内存（8 位），允许以二进制记数法表示 2^8=256 个值。char 类型可以是正数值也可以是负数值。值的范围从 -128 到 127。
    uchar：uchar 整数类型同样占用 1 字节内存，这和 char 类型是一样的，不同的是 uchar 仅用于正数值。最小的值为零，最大的值是 255。uchar 类型名称的第一个字母 u 是 unsigned（无符号）的缩写。
    short：short 类型的大小为 2 字节（16 位），相应地，它可以表示的值的范围为 2 的 16 次幂：2^16 = 65,536。 由于 short 类型是有符号的，它包含正数值和负数值，因此值的范围介于 -32,768 到 32,767 之间。
    ushort：无符号 short 类型即类型 ushort，后者的大小同样为 2 字节。最小值为 0，最大值为 65,535。
    int：int 类型的大小为 4 字节（32 位）。最小值为 -2,147,483,648，最大值为 2,147,483,647。
    uint：  无符号整数类型即 uint。它占用 4 字节内存，可表示从 0 至 4,294,967,295 的整数。
    long：long 类型的大小为 8 字节（64 位）。最小值为 -9,223,372,036,854,775,808，最大值为 9,223,372,036,854,775,807。
    ulong：ulong 类型同样占用 8 字节内存，可存储从 0 至 18,446,744,073,709,551,615 的值。