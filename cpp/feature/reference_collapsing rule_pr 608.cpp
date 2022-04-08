//通常情况下，不能将一个右值引用绑定到一个左值上
//下面这个情况貌似是不行的。f3接受右值引用，但传入的i是一个左值引用。
template <typename T> void f3(T&&);
int i = 42;
f3(i); //attention


//因为有两个特例规则：
//第一，将一个左值（如i）传递给函数的右值引用参数（&&），并且右值引用指向模板类型参数（T&&）。
//以上两个条件达成将启用第一个特例规则：
//编译器推断模板类型参数T为实值的左值引用类型。所以调用f3(i),将推断T的类型为int&。

//引用的引用时不能直接定义的，但是通过其他途径可以间接定义：类型别名/模板类型参数
//第二，如果间接创建一个引用的引用，则这些引用会形成折叠。
//右值引用的右值引用 -> 右值引用 T&& && -> T&&;
//其他的->左值引用: T& &, T& &&, T&& &;



//这两条规则是std::move工作的原理。
template <typename T>
typename remove_reference<T>::type&& move(T&& t)
{
    return static_cast<typename remove_reference<T>::type&&>(t);
}

//传给move一个右值
string s2;
s2 = std::move(string("bye!"));
//推断T的类型为string
//remove_reference<string>
//remove_reference<string>::type 是string
//move的返回类型是string&&
//move的函数参数t 是string&&
//实例化结果：string&& move(string &&)


//传给move一个左值
string s1("hi!");
s2 = std::move(s1);
//引用特例1，S1
