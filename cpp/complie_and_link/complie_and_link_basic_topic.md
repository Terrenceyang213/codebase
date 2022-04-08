# 1. C++ 运行基本原理

## 1.1 文件结构

> ./main.cpp

``` c++
// main.cpp
#include <iostream>

int main()
{
    std::cout << "Hello World!" << std::endl;
    std::cin.get();
}

```
## 1.2 细节讲解
- entry function
- main返回值：main函数不返回具体数值时默认返回0，这个特性只有main函数有
- `std::cout <<`:实际上是函数std::cout.print()的重载.也可写作`std::count.print("Hello World").print(std::endl); `

## 1.3 如何从.cpp到.exe
1. 预处理环节：处理#include/#define/#ifdef等预处理语句。
   - `#include <iostream>`:iostream中的所有内容将被拷贝到main.cpp中。
2. 文件编译：源代码被翻译成机器码
   - 编译阶段的选项会对编译行为产生直接影响。 
   - .h文件不会被编译，只会直接在被调用的.cpp文件中扩展
   - .cpp文件会被编译成为.obj文件
   - 这个阶段所有调用的函数和变量，只需要声明即可，编译器默认能找到其定义。
3. 链接：项目中的.obj文件被链接到一起，
   - 这个阶段中，所有的声明将被找到对应的定义。
  

# 2. C++ 运行基本原理2-多文件角度
将代码分接进多个文件

## 2.1 文件结构 1 - 问题的提出
> ./ main.cpp
> ./ log.cpp

``` c++
// log.cpp
void Log(const char* message)
{
    std::cout << message << std::endl;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>log.cpp
// 1>C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\log.cpp(3,7): error C2039: "cout": 不是 "std" 的成员
// 1>C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\predefined C++ types (compiler internal)(339): message : 参见“std”的声明
// 1>C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\log.cpp(3,12): error C2065: “cout”: 未声明的标识符
// 1>C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\log.cpp(3,31): error C2039: "endl": 不是 "std" 的成员
// 1>C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\predefined C++ types (compiler internal)(339): message : 参见“std”的声明
// 1>C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\log.cpp(3,35): error C2065: “endl”: 未声明的标识符
// 1>已完成生成项目“compile_and_link_multi-file.vcxproj”的操作 - 失败。
// ========== 生成: 成功 0 个，失败 1 个，最新 0 个，跳过 0 个 ==========
```

``` c++
// main.cpp
#include <iostream>

int main()
{
    Log("Hello World!");
    std::cin.get();
    return 0;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>main.cpp
// 1>C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\main.cpp(5,2): error C3861: “Log”: 找不到标识符
// 1>已完成生成项目“compile_and_link_multi-file.vcxproj”的操作 - 失败。
// ========== 生成: 成功 0 个，失败 1 个，最新 0 个，跳过 0 个 ==========
```
### 2.1.2 问题解析
log.cpp无法编译因为没有声明std，std的声明在iostream里面。c++中，任何使用到的变量都需要声明。

## 2.2 文件结构2 - 问题部分解决

> ./ main.cpp
> ./ log.cpp

``` c++
// log.cpp
#include <iostream> //<1>

void Log(const char* message)
{
    std::cout << message << std::endl;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>log.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

``` c++
// main.cpp
#include <iostream>

int main()
{
    Log("Hello World!");
    std::cin.get();
    return 0;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>main.cpp
// 1>C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\main.cpp(5,2): error C3861: “Log”: 找不到标识符
// 1>已完成生成项目“compile_and_link_multi-file.vcxproj”的操作 - 失败。
// ========== 生成: 成功 0 个，失败 1 个，最新 0 个，跳过 0 个 ==========
```

### 2.2.1 问题解析
1. Log找不着，因为main.cpp中没有Log的声明。
2. 声明：就是一种给编译器的承诺，编译当前obj文件的时候，这个变量/函数是存在的。
   1. 只需要声明函数的返回值，函数名，参数类型即可。
3. 定义：一个函数的具体函数体。


## 2.3 文件结构3 - 问题解决
> ./ main.cpp
> ./ log.cpp

``` c++
// log.cpp
#include <iostream>

void Log(const char* message)
{
    std::cout << message << std::endl;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>log.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

``` c++
// main.cpp

void Log(const char*); //<1> 甚至不需要形参名，但最好还是加上

int main()
{
    Log("Hello World!");
    std::cin.get();
    return 0;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>main.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

## 总结
编译的通过需要声明即可。


# 3. 如何通过声明找到确切的函数定义呢？

## 3.1 文件结构1 - 函数有声明无定义
> ./ main.cpp
> ./ log.cpp

``` c++
// log.cpp
#include <iostream>

void Logr(const char* message) //<1> 函数名被改为Logr
{
    std::cout << message << std::endl;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>log.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

``` c++
// main.cpp

void Log(const char*); 

int main()
{
    Log("Hello World!");
    std::cin.get();
    return 0;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>main.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

链接阶段：
``` c++
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>main.obj : error LNK2019: 无法解析的外部符号 "void __cdecl Log(char const *)" (?Log@@YAXPBD@Z)，函数 _main 中引用了该符号
// 1>C:\base\codebase\cpp\ProjectCode\Debug\compile_and_link_multi-file.exe : fatal error LNK1120: 1 个无法解析的外部命令
// 1>已完成生成项目“compile_and_link_multi-file.vcxproj”的操作 - 失败。
========== 生成: 成功 0 个，失败 1 个，最新 0 个，跳过 0 个 ==========
```

1. 文件单独编译没有问题
2. 链接报错
   1. 一个函数的标识：返回值、函数名、形参类型 `void __cdecl Log(char const *)`
   2. 编译系统内部函数ID：(?Log@@YAXPBD@Z)
   3. 这个错误是在obj文件中找不到Log的定义。

## 3.2 文件结构2 - 编译正确的情况

> ./ main.cpp
> ./ log.cpp

``` c++
// log.cpp
#include <iostream>

void Log(const char* message) //<1> 函数名被改为Logr
{
    std::cout << message << std::endl;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>log.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

``` c++
// main.cpp

void Log(const char*); 

int main()
{
    Log("Hello World!");
    std::cin.get();
    return 0;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>main.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

链接阶段：
``` c++
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>compile_and_link_multi-file.vcxproj -> C:\base\codebase\cpp\ProjectCode\Debug\compile_and_link_multi-file.exe
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

1. cpp文件被分别编译成为obj文件
2. obj文件中的各个声明，会在其他obj文件中关联至定义
   1. Log函数的定义最终定位到Log.obj

# 4. cpp编译器
1. 文件类型对cpp编译器来说没有意义，可以任意指定什么类型的文件作为任何输入。
2. 每个cpp文件都被翻译成为一个obj，因此一个cpp文件是一个翻译单元。

## 4.1 文件结构
> ./ main.cpp
> ./ log.cpp

``` c++
// log.cpp
#include <iostream>

void Log(const char* message) //<1> 函数名被改为Logr
{
    std::cout << message << std::endl;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>log.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

``` c++
// main.cpp
void Log(const char*); 

int main()
{
    Log("Hello World!");
    std::cin.get();
    return 0;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>main.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

``` c++
//Math.cpp
int Multipy(int a, int b)
{
    int result = 0;
    result = a * b;
    return result;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>Mathcpp.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```


链接阶段：
``` c++
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>compile_and_link_multi-file.vcxproj -> C:\base\codebase\cpp\ProjectCode\Debug\compile_and_link_multi-file.exe
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

## 4.2 问题的提出
同样编译的三个文件，但是大小却差别十倍以上。原因在于#include <iostream>

1. 在VS项目属性 - C/C++ - Preprocessor - Preprocess to a file：yes
2. 编译后会出现：Mathcpp.i文件




# 5 预处理阶段的运行原理
预处理：复制，替换#include/#define/

## 5.1 文件结构 - #include做了什么
> ./src/Math.cpp
> ./src/EndBrace.h

``` c++
//EndBrace.h
} //<1> 这个文件中就这一个符号。
```

``` c++
//Math.cpp
int Multipy(int a, int b)
{
    int result = 0;
    result = a * b;
    return result;
    //<1> without }
#include "EndBrace.h"

已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug Win32 ------
// 1>Mathcpp.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

``` c++
//Mathcpp.i
#line 1 "C:\\base\\codebase\\cpp\\ProjectCode\\compile_and_link_multi-file\\Mathcpp.cpp"
int Multipy(int a, int b)
{
	int result = 0;
	result = a * b;
	return result;
#line 1 "C:\\base\\codebase\\cpp\\ProjectCode\\compile_and_link_multi-file\\EndBrace.h" 

} //<1> #include
#line 7 "C:\\base\\codebase\\cpp\\ProjectCode\\compile_and_link_multi-file\\Mathcpp.cpp"

```

## 解析
头文件执行的就是一个粘贴赋值操作，无他

### 5.1.1 #include <iostream> 做了什么

``` c++
#include <iostream>

int Multipy(int a, int b)
{
	int result = 0;
	result = a * b;
	return result;
}
```



``` c++
// Mathcpp.i
// 上面省略6w行
// ......
 extern __declspec(dllimport) wistream wcin;
 extern __declspec(dllimport) wostream wcout;
 extern __declspec(dllimport) wostream wcerr;
 extern __declspec(dllimport) wostream wclog;
 extern __declspec(dllimport) wistream* _Ptr_wcin;
 extern __declspec(dllimport) wostream* _Ptr_wcout;
 extern __declspec(dllimport) wostream* _Ptr_wcerr;
 extern __declspec(dllimport) wostream* _Ptr_wclog;


class __declspec(dllimport) _Winit {
public:
    __thiscall _Winit();
    __thiscall ~_Winit() noexcept;

private:
     static int _Init_cnt;
};
#line 68 "D:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.28.29910\\include\\iostream"
}


#pragma warning(pop)
#pragma pack(pop)
#line 74 "D:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.28.29910\\include\\iostream"
#line 75 "D:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.28.29910\\include\\iostream"
#line 2 "C:\\base\\codebase\\cpp\\ProjectCode\\compile_and_link_multi-file\\Mathcpp.cpp"

int Multipy(int a, int b)
{
	int result = 0;
	result = a * b;
	return result;
}

```


## 5.2 文件结构2 - define做了什么

``` c++
#define INTEGER int

INTEGER Multipy(int a, int b)
{
	INTEGER result = 0;
	result = a * b;
	return result;
}
```

``` c++
#line 1 "C:\\base\\codebase\\cpp\\ProjectCode\\compile_and_link_multi-file\\Mathcpp.cpp"


int Multipy(int a, int b)
{
	int result = 0;
	result = a * b;
	return result;
}
```

## 5.3 文件结构 - #if
``` c++

#if 1
INTEGER Multipy(int a, int b)
{
	INTEGER result = 0;
	result = a * b;
	return result;
}
#endif
```

``` c++
#line 1 "C:\\base\\codebase\\cpp\\ProjectCode\\compile_and_link_multi-file\\Mathcpp.cpp"


int Multipy(int a, int b)
{
	int result = 0;
	result = a * b;
	return result;
}
#line 10 "C:\\base\\codebase\\cpp\\ProjectCode\\compile_and_link_multi-file\\Mathcpp.cpp"

```
如果条件未成立
``` c++
#if 0
INTEGER Multipy(int a, int b)
{
	INTEGER result = 0;
	result = a * b;
	return result;
}
#endif
```

``` c++
#line 1 "C:\\base\\codebase\\cpp\\ProjectCode\\compile_and_link_multi-file\\Mathcpp.cpp"

#line 10 "C:\\base\\codebase\\cpp\\ProjectCode\\compile_and_link_multi-file\\Mathcpp.cpp"
```

### 解析
#if可以决定代码是否使用。



# 6. 编译阶段：obj 文件是什么
输出汇编码
1. 项目属性 - C/C++ - 输出文件 - 汇编程序输出：仅有程序集的列表

``` c++
int Multipy(int a, int b)
{
	int result = 0;
	result = a * b;
	return result;
}
```

``` asm

; Listing generated by Microsoft (R) Optimizing Compiler Version 19.28.29913.0 

include listing.inc

INCLUDELIB MSVCRTD
INCLUDELIB OLDNAMES

msvcjmc	SEGMENT
__E6172F3F_Mathcpp@cpp DB 01H
msvcjmc	ENDS
PUBLIC	?Multipy@@YAHHH@Z				; Multipy
PUBLIC	__JustMyCode_Default
EXTRN	_RTC_InitBase:PROC
EXTRN	_RTC_Shutdown:PROC
EXTRN	__CheckForDebuggerJustMyCode:PROC
;	COMDAT pdata
pdata	SEGMENT
$pdata$?Multipy@@YAHHH@Z DD imagerel $LN3
	DD	imagerel $LN3+92
	DD	imagerel $unwind$?Multipy@@YAHHH@Z
pdata	ENDS
;	COMDAT rtc$TMZ
rtc$TMZ	SEGMENT
_RTC_Shutdown.rtc$TMZ DQ FLAT:_RTC_Shutdown
rtc$TMZ	ENDS
;	COMDAT rtc$IMZ
rtc$IMZ	SEGMENT
_RTC_InitBase.rtc$IMZ DQ FLAT:_RTC_InitBase
rtc$IMZ	ENDS
;	COMDAT xdata
xdata	SEGMENT
$unwind$?Multipy@@YAHHH@Z DD 025052c01H
	DD	01112316H
	DD	0700a0021H
	DD	05009H
xdata	ENDS
; Function compile flags: /Odt
;	COMDAT __JustMyCode_Default
_TEXT	SEGMENT
__JustMyCode_Default PROC				; COMDAT
	ret	0
__JustMyCode_Default ENDP
_TEXT	ENDS
; Function compile flags: /Odtp /RTCsu /ZI
;	COMDAT ?Multipy@@YAHHH@Z
_TEXT	SEGMENT
result$ = 4
a$ = 256
b$ = 264
?Multipy@@YAHHH@Z PROC					; Multipy, COMDAT
; File C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\Mathcpp.cpp
; Line 2
$LN3:
	mov	DWORD PTR [rsp+16], edx
	mov	DWORD PTR [rsp+8], ecx
	push	rbp
	push	rdi
	sub	rsp, 264				; 00000108H
	lea	rbp, QWORD PTR [rsp+32]
	mov	rdi, rsp
	mov	ecx, 66					; 00000042H
	mov	eax, -858993460				; ccccccccH
	rep stosd
	mov	ecx, DWORD PTR [rsp+296]
	lea	rcx, OFFSET FLAT:__E6172F3F_Mathcpp@cpp
	call	__CheckForDebuggerJustMyCode
; Line 3
	mov	DWORD PTR result$[rbp], 0
; Line 4
	mov	eax, DWORD PTR a$[rbp]
	imul	eax, DWORD PTR b$[rbp]
	mov	DWORD PTR result$[rbp], eax
; Line 5
	mov	eax, DWORD PTR result$[rbp]
; Line 6
	lea	rsp, QWORD PTR [rbp+232]
	pop	rdi
	pop	rbp
	ret	0
?Multipy@@YAHHH@Z ENDP					; Multipy
_TEXT	ENDS
END


```

# 7. 代码优化
1. 编译器优化：O2
2. 代码生成 - basic runtime checks：default

## 7.1 文件结构 - 优化选项对汇编码的影响

``` c++
int Multipy(int a, int b)
{
	int result = 0;
	result = a * b;
	return result;
}
```

汇编文件极大简化。


## 7.2 文件结构2 - 对于一些情况编译器会主动进行优化
``` c++
int Multipy()
{

	return 2 * 5;
}
```

``` 
_TEXT	SEGMENT
?Multipy@@YAHXZ PROC					; Multipy, COMDAT
; File C:\base\codebase\cpp\ProjectCode\compile_and_link_multi-file\Mathcpp.cpp
; Line 2
$LN3:
	push	rbp
	sub	rsp, 96					; 00000060H
	lea	rbp, QWORD PTR [rsp+32]
	lea	rcx, OFFSET FLAT:__E6172F3F_Mathcpp@cpp
	call	__CheckForDebuggerJustMyCode
; Line 3
	mov	eax, 10  //<1>: 直接返回了10，而不是2*5
; Line 4
	lea	rsp, QWORD PTR [rbp+64]
	pop	rbp
	ret	0
?Multipy@@YAHXZ ENDP					; Multipy
_TEXT	ENDS
END


```

## 7.3 文件结构3 - 可优化操作
``` c++
const char* Log(const char * message)
{
    return message
}
int Multipy()
{
    Log("Multiply");
	return a * b;
}
```
Log函数什么都没做，在优化选项打开后将被忽略掉。

# 8 链接器linker

## 8.1 编译和链接的区别
- ctrl+F7：仅编译
- 对项目build：编译+链接

## 8.2 链接示例

### 8.2.1 文件结构
> Math.cpp
> 
``` c++
//Math.cpp
#include <iostream>

void Log(const char * message)
{
	std::cout<< message<< std::endl;
}

int Multiply(int a , int b)
{
	Log("Hello World!");
	return a * b;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug x64 ------
// 1>MSVCRTD.lib(exe_main.obj) : error LNK2019: 无法解析的外部符号 main，函数 "int __cdecl invoke_main(void)" (?invoke_main@@YAHXZ) 中引用了该符号
// 1>C:\base\codebase\cpp\ProjectCode\x64\Debug\compile_and_link_multi-file.exe : fatal error LNK1120: 1 个无法解析的外部命令
// 1>已完成生成项目“compile_and_link_multi-file.vcxproj”的操作 - 失败。
// ========== 生成: 成功 0 个，失败 1 个，最新 0 个，跳过 0 个 ==========
```

``` c++
// configuration type:dll

// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug x64 ------
// 1>Mathcpp.cpp
// 1>compile_and_link_multi-file.vcxproj -> C:\base\codebase\cpp\ProjectCode\x64\Debug\compile_and_link_multi-file.dll
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

LNK开头的是编译错误，C开头的是编译错误。

### 8.2.2 entry point
- 配置类型configuration type为exe必须有一个main函数作为入口
- 其他类型的如dll，lib则并不必须有一个入口。
- 链接器的高级选项中可以更换entry point
  - 如何更换入口点？
- 在当前文件中，没有使用的函数，即使没有定义，也不会编译错误。
  - 但是会报链接错误。
  - 但如果这个函数明确定义为static，即仅在本文件内使用，不需要进行链接，那么即使他内部使用了需要链接的函数，只要他自身没被使用，就能生成。
  

## 8.3 static：如果一个函数仅在当前文件中使用，不需要进行链接

### 8.3.1 文件结构
> Math.cpp
> Log.cpp
``` c++
//Log.cpp
#include <iostream>
void Logr(const char * message)
{
	std::cout<< message << std::endl;
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug x64 ------
// 1>Log.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

``` c++
// Math.cpp
#include <iostream>

void Log(const char * message); //<1> 这个函数名是有问题的

int Multiply(int a , int b)
{
	Log("Hello World!");
	return a * b;
}

int main()
{
	std::cout << Multiply(5, 8) << std::endl;
	std::cin.get();
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug x64 ------
// 1>Mathcpp.cpp
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

链接是肯定会报错的。
``` c++
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug x64 ------
// 1>Log.cpp
// 1>Mathcpp.obj : error LNK2019: 无法解析的外部符号 "void __cdecl Log(char const *)" (?Log@@YAXPEBD@Z)，函数 "int __cdecl Multiply(int,int)" (?Multiply@@YAHHH@Z) 中引用了该符号
// 1>C:\base\codebase\cpp\ProjectCode\x64\Debug\compile_and_link_multi-file.exe : fatal error LNK1120: 1 个无法解析的外部命令
// 1>已完成生成项目“compile_and_link_multi-file.vcxproj”的操作 - 失败。
// ========== 生成: 成功 0 个，失败 1 个，最新 0 个，跳过 0 个 ==========
```

### 8.3.2 解析
cpp文件中将Multiply改为static，则只要不使用这个函数，则连接可以成功
``` c++
// Math.cpp
#include <iostream>

void Log(const char * message); //<1> 这个函数名是有问题的

static int Multiply(int a , int b)
{
	Log("Hello World!");
	return a * b;
}

int main()
{
	//std::cout << Multiply(5, 8) << std::endl;
	std::cin.get();
}
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug x64 ------
// 1>Mathcpp.cpp 
// 1>compile_and_link_multi-file.vcxproj -> C:\base\codebase\cpp\ProjectCode\x64\Debug\compile_and_link_multi-file.exe
// ========== 生成: 成功 1 个，失败 0 个，最新 0 个，跳过 0 个 ==========
```

可以看到链接阶段忽略了Log.cpp


## 9. 链接阶段 - 模糊定义
当对于同一个函数声明，存在两处定义时，就会出发链接错误：模糊定义。

### 
> Math.cpp
> Log.cpp

``` c++
// Log.cpp
#include <iostream>

void Log(const char* message)
{
	std::cout << message << std::endl;
}
```

``` c++
// Math.cpp
#include <iostream>

void Log(const char* message);

void Log(const char* message) //<1> 给出一个重复定义
{
	std::cout << message << std::endl;
}

int Multiply(int a, int b)
{
	Log("Hello World");
	return a * b;
}

int main()
{
	std::cout << Multiply(5, 8) << std::endl;
	std::cin.get();
}
```

编译都能通过，链接会出问题
``` c++
// 已启动生成…
// 1>------ 已启动生成: 项目: compile_and_link_multi-file, 配置: Debug x64 ------
// 1>Log.cpp
// 1>Mathcpp.cpp
// 1>正在生成代码...
// 1>LINK : 没有找到 C:\base\codebase\cpp\ProjectCode\x64\Debug\compile_and_link_multi-file.exe 或上一个增量链接没有生成它；正在执行完全链接
// 1>Mathcpp.obj : error LNK2005: "void __cdecl Log(char const *)" (?Log@@YAXPEBD@Z) 已经在 Log.obj 中定义
// 1>C:\base\codebase\cpp\ProjectCode\x64\Debug\compile_and_link_multi-file.exe : fatal error LNK1169: 找到一个或多个多重定义的符号
// 1>已完成生成项目“compile_and_link_multi-file.vcxproj”的操作 - 失败。
// ========== 生成: 成功 0 个，失败 1 个，最新 0 个，跳过 0 个 ==========
```

## 10. 便于链接的成功实践

定义为什么最好不用出现在.h文件中，因为结合上一节的内容。当在多个cpp文件中include同一个.h文件时。
一旦文件展开，就会出现多处相同的定义。

### 声明在.h文件中，而定义在cpp文件中。
``` c++
//Log.h
#pragma once

void Log(const char* message);
```

``` c++
//Log.cpp
#include <iostream>
#include "Log.h" //<1> 为什么源文件要包含对应的头文件

void InitLog()
{
	Log("Init Log");
}

void Log(const char* message)
{
	std::cout << message << std::endl;
}
```

``` c++
#include <iostream>
#include "Log.h"
int Multiply(int a, int b)
{
	Log("Hello World");
	return a * b;
}

int main()
{
	std::cout << Multiply(5, 8) << std::endl;
	std::cin.get();
}
```

### static
但是还有另一种备选，即定义在.h文件中的函数是静态函数。这样，在展开后，所有包含.h的cpp文件会各有一个自己版本的定义，并且不参与链接。
``` c++
//Log.h
#pragma once

inline void Log(const char* message)
{
	std::cout << message << std::endl;
}
```

``` c++
//Log.cpp
#include <iostream>
#include "Log.h"

void InitLog()
{
	Log("Init Log");
}
```

``` c++
#include <iostream>
#include "Log.h"

int Multiply(int a, int b)
{
	Log("Hello World");
	return a * b;
}

int main()
{
	std::cout << Multiply(5, 8) << std::endl;
	std::cin.get();
}
```



### inline
就是.h种的定义是inline，这样在编译时就会被直接替换成函数体。

``` c++
//Log.h
#pragma once

static void Log(const char* message)
{
	std::cout << message << std::endl;
}
```

``` c++
//Log.cpp
#include <iostream>
#include "Log.h"

void InitLog()
{
	Log("Init Log");
}
```

``` c++
#include <iostream>

void Log(const char* message);

int Multiply(int a, int b)
{
	Log("Hello World");
	return a * b;
}

int main()
{
	std::cout << Multiply(5, 8) << std::endl;
	std::cin.get();
}
```






### 为什么要在源文件中包含对应的头文件
1. 为了免除先后定义对依赖的影响
   1. func.cpp中：
      1. funca先定义，funcb后定义，则funca不能调用funcb。
      2. funca之前必须出现funcb的声明才行
      3. 那么最好的方式就是统一在头文件中声明，然后cpp中包含头文件
   2. 对内对外接口问题
      1. 头文件的确实对外的接口，当cpp文件中需要调用外部函数时，必须声明
      2. 但是在cpp文件中声明外部函数是糟糕的
      3. 因此最好在头文件中声明
   3. 可以设计对内对外两个头文件。
      1. 对内头文件，即static，仅对内使用
      2. 对外头文件为对外调用。


