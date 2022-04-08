https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown#cmd-markdown-%E9%AB%98%E9%98%B6%E8%AF%AD%E6%B3%95%E6%89%8B%E5%86%8C

# 
## 行内公式
$ J_\alpha(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma (m + \alpha + 1)} {\left({ \frac{x}{2} }\right)}^{2m + \alpha} \text {，行内公式示例} $

## 独立公式
$$ J_\alpha(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma (m + \alpha + 1)} {\left({ \frac{x}{2} }\right)}^{2m + \alpha} \text {，独立公式示例} $$


# 符号

## 上标下标

$$ x^{y^z}=(1+{\rm e}^x)^{-2xy^w} $$

## 上下左右标
$$ \sideset{^1_2}{^3_4}\bigotimes $$

## 括号与分割符

()、[] 和 | 表示符号本身，使用 \{\} 来表示 {} 。当要显示大号的括号或分隔符时，要用 \left 和 \right 命令。

$$
\langle \rangle 	\\
\lceil 	\rceil  \\
\lfloor \rfloor \\
\lbrace \rbrace 	
$$

$$ f(x,y,z) = 3y^2z \left( 3+\frac{7x+5}{1+y^2} \right) $$

### 有时候要用 \left. 或 \right. 进行匹配而不显示本身。
$$ \left. \frac{{\rm d}u}{{\rm d}x} \right| _{x=0} $$

## 分数
$$\frac{a-1}{b-1} \quad and \quad {a+1\over b+1}$$

## 开方
$$\sqrt{2} \quad and \quad \sqrt[n]{3}$$

## 省略号
$$f(x_1,x_2,\underbrace{\ldots}_{\rm l:ldots} ,x_n) = x_1^2 + x_2^2 + \underbrace{\cdots}_{\rm l:cdots} + x_n^2$$


## 矢量
$$\vec{a} \cdot \vec{b}=0$$
$$\overleftarrow{xy} \quad and \quad \overleftrightarrow{xy} \quad and \quad \overrightarrow{xy}$$

## 积分
$$\int_0^1 {x^2} \,{\rm d}x$$

## 极限
$$ \lim_{n \to +\infty} \frac{1}{n(n+1)} \quad and \quad \lim_{x\leftarrow{示例}} \frac{1}{n(n+1)} $$

## 累加累乘法
$$\sum_{i=1}^n \frac{1}{i^2} $$ 
$$\quad \prod_{i=1}^n \frac{1}{i^2} $$
$$\quad \bigcup_{i=1}^{2} R$$

## 希腊字母
$$
\alpha 	    A 	        \beta 	    B  \\
\gamma 		\Gamma 	    \delta 	 	\Delta\\
\epsilon 	E 	        \zeta 	    Z \\
\eta 		H 	        \theta 	    \Theta \\
\iota 		I 	        \kappa 	    K   \\
\lambda 	\Lambda 	\mu 	     M\\
\nu 		N 	        \xi 	 	\Xi\\
o 		    O 	        \pi 		\Pi\\
\rho 		P 	        \sigma 	 	\Sigma\\
\tau 	 	T 	        \upsilon 	\Upsilon\\
\phi 		\Phi 	    \chi  	    X\\
\psi 	 	\Psi 	    \omega 	    \Omega 	
$$

### 希腊字母特殊形式
$$
\epsilon \to E \to \varepsilon \\
\theta \to \Theta \to \vartheta \\
\rho \to P \to \varrho \\
\sigma \to \Sigma \to \varsigma \\
\phi \to \Phi \to \varphi 
$$

## 关系运算符
$$
\pm | \times | \div | \mid \\
\nmid | \cdot | \circ | \ast \\
\bigodot | \bigotimes | \bigoplus | \leq \\
\geq | \neq | \approx | \equiv \\
\sum | \prod | \coprod | \backslash 
$$

## 集合运算符
$$
\emptyset | \in | \notin \\
\subset | \supset | \subseteq \\
\supseteq | \bigcap | \bigcup \\
\bigvee | \bigwedge | \biguplus 
$$

## 对数运算符
$$
\log | \lg | \ln
$$

## 三角运算符
$$
30^\circ  | \bot | \angle A \\
\sin | \cos | \tan \\
\csc | \sec | \cot
$$

## 微积分
$$
\int | \iint | \iiint \\
\iiiint | \oint | \prime \\ 
\lim 	| \infty | \nabla \\
$$

## 逻辑运算符

$$
\because \therefore \\
\forall \exists \not\subset \\
\not< \not> \not=
$$

## 戴帽符号
$$
\hat{xy} \widehat{xyz} \\
\tilde{xy} \widetilde{xyz} \\
\check{x} \breve{y} \\
\grave{x}  \acute{y}
$$

## 连线
$$
\fbox{a+b+c+d} \\
\overleftarrow{a+b+c+d}\\
\overrightarrow{a+b+c+d} \\
\overleftrightarrow{a+b+c+d} \\
\underleftarrow{a+b+c+d} \\
\underrightarrow{a+b+c+d}\\
\underleftrightarrow{a+b+c+d} \\
\overline{a+b+c+d} \\
\underline{a+b+c+d} \\
\overbrace{a+b+c+d}^{Sample} \\
\underbrace{a+b+c+d}_{Sample} \\
\overbrace{a+\underbrace{b+c}_{1.0}+d}^{2.0} \\
\underbrace{a\cdot a\cdots a}_{b\text{ times}} 
$$

## 箭头符号

$$
    |\to |\mapsto| \\
    |\implies| \iff| \impliedby|
$$
 
 $$
    |\uparrow|\Uparrow| \\
    |\downarrow|\Downarrow| \\
    |\leftarrow||\Leftarrow| \\
    |\rightarrow||\Rightarrow| \\
    |\leftrightarrow|\Leftrightarrow|\\
    |\longleftarrow|\Longleftarrow|\\
    |\longrightarrow|\Longrightarrow|\\
    |\longleftrightarrow|\Longleftrightarrow|
$$

## 字体转换
$$
|罗马体|\rm{Sample}|花体|\cal{SAMPLE}|\\
|意大利体|\it{Sample}|黑板粗体|\Bbb{SAMPLE}|\\
|粗体|\bf{Sample}|数学斜体|\mit{SAMPLE}|\\
|等线体|\sf{Sample}|手写体|\scr{SAMPLE}|\\
|打字机体|\tt{Sample}
|旧德式字体|\frak{Sample}|
$$

$$
\mathrm{Bad} \quad \mathrm{Better} \\
\int_0^1 x^2 dx \quad \int_0^1 x^2 \,{\rm d}x 
$$

## 大括号和行标的使用

使用 \left 和 \right 来创建自动匹配高度的 (圆括号)，[方括号] 和 {花括号} 。
在每个公式末尾前使用 \tag{行标} 来实现行标。
$$
f\left(
   \left[ 
     \frac{
       1+\left\{x,y\right\}
     }{
       \left(
          \frac{x}{y}+\frac{y}{x}
       \right)
       \left(u+1\right)
     }+a
   \right]^{3/2}
\right)
\tag{行标}
$$

$$
\begin{aligned}
a=&\left(1+2+3+  \cdots \right. \\
& \cdots+ \left. \infty-2+\infty-1+\infty\right)
\end{aligned}
$$

如果你需要将行内显示的分隔符也变大，可以使用 \middle 命令：
$$
\left\langle  
  q
\middle|
  \frac{\frac{x}{y}}{\frac{u}{v}}
\middle| 
   p 
\right\rangle
$$

## 定义新的符号 \operatorname

$$ \operatorname{Symbol} A $$

## 添加注释文字 \text
$$ f(n)= \begin{cases} n/2, & \text {if $n$ is even} \\ 3n+1, & \text{if $n$ is odd} \end{cases} $$

## 在字符间加入空格
$$ a \, b \mid a \; b \mid a \quad b \mid a \qquad b $$

## 更改字体颜色
$$
\begin{array}{|rrrrrrrr|}\hline
\verb+#000+ & \color{#000}{text} & & &
\verb+#00F+ & \color{#00F}{text} & & \\
& & \verb+#0F0+ & \color{#0F0}{text} &
& & \verb+#0FF+ & \color{#0FF}{text}\\
\verb+#F00+ & \color{#F00}{text} & & &
\verb+#F0F+ & \color{#F0F}{text} & & \\
& & \verb+#FF0+ & \color{#FF0}{text} &
& & \verb+#FFF+ & \color{#FFF}{text}\\
\hline
\end{array}
$$

$$
\begin{array}{|rrrrrrrr|}
\hline
\verb+#000+ & \color{#000}{text} & \verb+#005+ & \color{#005}{text} & \verb+#00A+ & \color{#00A}{text} & \verb+#00F+ & \color{#00F}{text}  \\
\verb+#500+ & \color{#500}{text} & \verb+#505+ & \color{#505}{text} & \verb+#50A+ & \color{#50A}{text} & \verb+#50F+ & \color{#50F}{text}  \\
\verb+#A00+ & \color{#A00}{text} & \verb+#A05+ & \color{#A05}{text} & \verb+#A0A+ & \color{#A0A}{text} & \verb+#A0F+ & \color{#A0F}{text}  \\
\verb+#F00+ & \color{#F00}{text} & \verb+#F05+ & \color{#F05}{text} & \verb+#F0A+ & \color{#F0A}{text} & \verb+#F0F+ & \color{#F0F}{text}  \\
\hline
\verb+#080+ & \color{#080}{text} & \verb+#085+ & \color{#085}{text} & \verb+#08A+ & \color{#08A}{text} & \verb+#08F+ & \color{#08F}{text}  \\
\verb+#580+ & \color{#580}{text} & \verb+#585+ & \color{#585}{text} & \verb+#58A+ & \color{#58A}{text} & \verb+#58F+ & \color{#58F}{text}  \\
\verb+#A80+ & \color{#A80}{text} & \verb+#A85+ & \color{#A85}{text} & \verb+#A8A+ & \color{#A8A}{text} & \verb+#A8F+ & \color{#A8F}{text}  \\
\verb+#F80+ & \color{#F80}{text} & \verb+#F85+ & \color{#F85}{text} & \verb+#F8A+ & \color{#F8A}{text} & \verb+#F8F+ & \color{#F8F}{text}  \\
\hline
\verb+#0F0+ & \color{#0F0}{text} & \verb+#0F5+ & \color{#0F5}{text} & \verb+#0FA+ & \color{#0FA}{text} & \verb+#0FF+ & \color{#0FF}{text}  \\
\verb+#5F0+ & \color{#5F0}{text} & \verb+#5F5+ & \color{#5F5}{text} & \verb+#5FA+ & \color{#5FA}{text} & \verb+#5FF+ & \color{#5FF}{text}  \\
\verb+#AF0+ & \color{#AF0}{text} & \verb+#AF5+ & \color{#AF5}{text} & \verb+#AFA+ & \color{#AFA}{text} & \verb+#AFF+ & \color{#AFF}{text}  \\
\verb+#FF0+ & \color{#FF0}{text} & \verb+#FF5+ & \color{#FF5}{text} & \verb+#FFA+ & \color{#FFA}{text} & \verb+#FFF+ & \color{#FFF}{text}  \\
\hline
\end{array}
$$

## 删除线
使用删除线功能必须声明 $$ 符号。

在公式内使用 \require{cancel} 来允许 片段删除线 的显示。
声明片段删除线后，使用 \cancel{字符}、\bcancel{字符}、\xcancel{字符} 和 \cancelto{字符} 来实现各种片段删除线效果。


$$
\require{cancel}\begin{array}{rl}
\verb|y+\cancel{x}| & y+\cancel{x}\\
\verb|\cancel{y+x}| & \cancel{y+x}\\
\verb|y+\bcancel{x}| & y+\bcancel{x}\\
\verb|y+\xcancel{x}| & y+\xcancel{x}\\
\verb|y+\cancelto{0}{x}| & y+\cancelto{0}{x}\\
\verb+\frac{1\cancel9}{\cancel95} = \frac15+& \frac{1\cancel9}{\cancel95} = \frac15 \\
\end{array}
$$


# 矩阵
## 如何输入无框矩阵

在开头使用 begin{matrix}，在结尾使用 end{matrix}，在中间插入矩阵元素，每个元素之间插入 & ，并在每行结尾处使用 \\ 。
使用矩阵时必须声明 $ 或 $$ 符号。

$$
        \begin{matrix}
        1 & x & x^2 \\
        1 & y & y^2 \\
        1 & z & z^2 \\
        \end{matrix}
$$


## 如何输入边框矩阵

在开头将 matrix 替换为 pmatrix bmatrix Bmatrix vmatrix Vmatrix 。
$ \begin{matrix} 1 & 2 \\ 3 & 4 \\ \end{matrix} $
$ \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ \end{pmatrix} $
$ \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ \end{bmatrix} $
$ \begin{Bmatrix} 1 & 2 \\ 3 & 4 \\ \end{Bmatrix} $
$ \begin{vmatrix} 1 & 2 \\ 3 & 4 \\ \end{vmatrix} $
$ \begin{Vmatrix} 1 & 2 \\ 3 & 4 \\ \end{Vmatrix} $

## 矩阵中的省略号
$$
        \begin{pmatrix}
        1 & a_1 & a_1^2 & \cdots & a_1^n \\
        1 & a_2 & a_2^2 & \cdots & a_2^n \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        1 & a_m & a_m^2 & \cdots & a_m^n \\
        \end{pmatrix}
$$


## 如何输入带分割符号的矩阵
$$
\left[
    \begin{array}{cc|c}
      1&2&3\\
      4&5&6
    \end{array}
\right]
$$

## 如何输入行中矩阵
这是一个行中矩阵的示例 $\bigl( \begin{smallmatrix} a & b \\ c & d \end{smallmatrix} \bigr)$ 。


# 方程式
## 如何输入一个方程式序列

人们经常想要一列整齐且居中的方程式序列。使用 \begin{align}…\end{align} 来创造一列方程式，其中在每行结尾处使用 \\ 。
使用方程式序列无需声明公式符号  dollor dumdollar。

$$
\begin{align}
\sqrt{37} & = \sqrt{\frac{73^2-1}{12^2}} \\
 & = \sqrt{\frac{73^2}{12^2}\cdot\frac{73^2-1}{73^2}} \\ 
 & = \sqrt{\frac{73^2}{12^2}}\sqrt{\frac{73^2-1}{73^2}} \\
 & = \frac{73}{12}\sqrt{1 - \frac{1}{73^2}} \\ 
 & \approx \frac{73}{12}\left(1 - \frac{1}{2\cdot73^2}\right)
\end{align}
$$

## 在一个方程式序列的每一行中注明原因

$$
\begin{align}
   v + w & = 0  &\text{Given} \tag 1\\
   -w & = -w + 0 & \text{additive identity} \tag 2\\
   -w + 0 & = -w + (v + w) & \text{equations $(1)$ and $(2)$}
\end{align}
$$


# 条件表达式使用参考

## 如何输入一个条件表达式

使用 begin{cases} 来创造一组条件表达式，在每一行条件中插入 & 来指定需要对齐的内容，并在每一行结尾处使用 \\，以 end{cases} 结束。

$$
        f(n) =
        \begin{cases}
        n/2,  & \text{if $n$ is even} \\
        3n+1, & \text{if $n$ is odd}
        \end{cases}
$$

## 如何输入一个左侧对齐的条件表达式

$$
        \left.
        \begin{array}{l}
        \text{if $n$ is even:}&n/2\\
        \text{if $n$ is odd:}&3n+1
        \end{array}
        \right\}
        =f(n)
$$


## 如何使条件表达式适配行高
在一些情况下，条件表达式中某些行的行高为非标准高度，此时使用 \\[2ex] 语句代替该行末尾的 \\ 来让编辑器适配。
一个 [ex] 指一个 "X-Height"，即x字母高度。可以根据情况指定多个 [ex]，如 [3ex]、[4ex] 等。
其实可以在任何地方使用 \\[2ex] 语句，只要你觉得合适。
$$
f(n) = 
\begin{cases}
\frac{n}{2},  & \text{if $n$ is even} \\
3n+1, & \text{if $n$ is odd}
\end{cases}
$$

$$
f(n) = 
\begin{cases}
\frac{n}{2},  & \text{if $n$ is even} \\[2ex]
3n+1, & \text{if $n$ is odd}
\end{cases}
$$

# 数组与表格使用参考

## 如何输入一个数组或表格

通常，一个格式化后的表格比单纯的文字或排版后的文字更具有可读性。数组和表格均以 begin{array} 开头，并在其后定义列数及每一列的文本对齐属性，c l r 分别代表居中、左对齐及右对齐。若需要插入垂直分割线，在定义式中插入 | ，若要插入水平分割线，在下一行输入前插入 \hline 。与矩阵相似，每行元素间均须要插入 & ，每行元素以 \\ 结尾，最后以 end{array} 结束数组。使用单个数组或表格时无需声明 $ 或 $$ 符号。
$$
\begin{array}{c|lcr}
n & \text{左对齐} & \text{居中对齐} & \text{右对齐} \\
\hline
1 & 0.24 & 1 & 125 \\
2 & -1 & 189 & -8 \\
3 & -20 & 2000 & 1+10i
\end{array}
$$

## 如何输入一个嵌套的数组或表格
多个数组/表格可 互相嵌套 并组成一组数组/一组表格。
使用嵌套前必须声明 dollar符号。

$$
\begin{array}{c}
    \begin{array}{cc}
        \begin{array}{c|cccc}
        \text{min} & 0 & 1 & 2 & 3\\
        \hline
        0 & 0 & 0 & 0 & 0\\
        1 & 0 & 1 & 1 & 1\\
        2 & 0 & 1 & 2 & 2\\
        3 & 0 & 1 & 2 & 3
        \end{array}
    &
        \begin{array}{c|cccc}
        \text{max}&0&1&2&3\\
        \hline
        0 & 0 & 1 & 2 & 3\\
        1 & 1 & 1 & 2 & 3\\
        2 & 2 & 2 & 2 & 3\\
        3 & 3 & 3 & 3 & 3
        \end{array}
    \end{array}
    \\
        \begin{array}{c|cccc}
        \Delta&0&1&2&3\\
        \hline
        0 & 0 & 1 & 2 & 3\\
        1 & 1 & 0 & 1 & 2\\
        2 & 2 & 1 & 0 & 1\\
        3 & 3 & 2 & 1 & 0
        \end{array}
\end{array}
$$

## 如何输入一个方程组
$$
\left\{ 
\begin{array}{c}
a_1x+b_1y+c_1z=d_1 \\ 
a_2x+b_2y+c_2z=d_2 \\ 
a_3x+b_3y+c_3z=d_3
\end{array}
\right. 
$$

$$
\begin{cases}
a_1x+b_1y+c_1z=d_1 \\ 
a_2x+b_2y+c_2z=d_2 \\ 
a_3x+b_3y+c_3z=d_3
\end{cases}
$$

# 连分数使用参考
## 如何输入一个连分式

就像输入分式时使用 \frac 一样，使用 \cfrac 来创建一个连分数。

$$
x = a_0 + \cfrac{1^2}{a_1
          + \cfrac{2^2}{a_2
          + \cfrac{3^2}{a_3 + \cfrac{4^4}{a_4 + \cdots}}}}
$$

$$
x = a_0 + \frac{1^2}{a_1
          + \frac{2^2}{a_2
          + \frac{3^2}{a_3 + \frac{4^4}{a_4 + \cdots}}}}
$$

$$
x = a_0 + \frac{1^2}{a_1+}
          \frac{2^2}{a_2+}
          \frac{3^2}{a_3 +} \frac{4^4}{a_4 +} \cdots
$$

# 交换图表使用参考
## 如何输入一个交换图表

使用一行 $ \require{AMScd} $ 语句来允许交换图表的显示。
声明交换图表后，语法与矩阵相似，在开头使用 begin{CD}，在结尾使用 end{CD}，在中间插入图表元素，每个元素之间插入 & ，并在每行结尾处使用 \\ 。

$$ 
\require{AMScd}$
\begin{CD}
    A @>a>> B\\
    @V b VV\# @VV c V\\
    C @>>d> D
\end{CD}
$$
其中，@>>> 代表右箭头、@<<< 代表左箭头、@VVV 代表下箭头、@AAA 代表上箭头、@= 代表水平双实线、@| 代表竖直双实线、@.代表没有箭头。
在 @>>> 的 >>> 之间任意插入文字即代表该箭头的注释文字。

$$
\begin{CD}
    A @>>> B @>{\text{very long label}}>> C \\
    @. @AAA @| \\
    D @= E @<<< F
\end{CD}
$$

# 其他注意事项

## 1
These are issues that won't affect the correctness of formulas, but might make them look significantly better or worse. Beginners should feel free to ignore this advice; someone else will correct it for them, or more likely nobody will care.

现在指出的小问题并不会影响方程式及公式等的正确显示，但能让它们看起来明显更好看。初学者可无视这些建议，自然会有强迫症患者替你们改掉它的，或者更可能地，根本没人发现这些问题。

Don't use \frac in exponents or limits of integrals; it looks bad and can be confusing, which is why it is rarely done in professional mathematical typesetting. Write the fraction horizontally, with a slash:

在以e为底的指数函数、极限和积分中尽量不要使用 \frac 符号：它会使整段函数看起来很怪，而且可能产生歧义。也正是因此它在专业数学排版中几乎从不出现。
横着写这些分式，中间使用斜线间隔 / （用斜线代替分数线）。

$$
\begin{array}{cc}
\mathrm{Bad} & \mathrm{Better} \\
\hline \\
e^{i\frac{\pi}2} \quad e^{\frac{i\pi}2}& e^{i\pi/2} \\
\int_{-\frac\pi2}^\frac\pi2 \sin x\,dx & \int_{-\pi/2}^{\pi/2}\sin x\,dx \\
\end{array}
$$

## 2
The | symbol has the wrong spacing when it is used as a divider, for example in set comprehensions. Use \mid instead:

| 符号在被当作分隔符时会产生错误的间隔，因此在需要分隔时最好使用 \mid 来代替它

$$
\begin{array}{cc}
\mathrm{Bad} & \mathrm{Better} \\
\hline \\
\{x|x^2\in\Bbb Z\} & \{x\mid x^2\in\Bbb Z\} \\
\end{array}
$$

## 3
For double and triple integrals, don't use \int\int or \int\int\int. Instead use the special forms \iint and \iiint:

使用多重积分符号时，不要多次使用 \int 来声明，直接使用 \iint 来表示 二重积分 ，使用 \iiint 来表示 三重积分 等。对于无限次积分，可以用 \int \cdots \int 表示。

$$
\begin{array}{cc}
\mathrm{Bad} & \mathrm{Better} \\
\hline \\
\int\int_S f(x)\,dy\,dx & \iint_S f(x)\,dy\,dx \\
\int\int\int_V f(x)\,dz\,dy\,dx & \iiint_V f(x)\,dz\,dy\,dx
\end{array}
$$

## 4
Use \,, to insert a thin space before differentials; without this $\TeX$ will mash them together:

在微分符号前加入 \, 来插入一个小的间隔空隙；没有 \, 符号的话，$\TeX$ 将会把不同的微分符号堆在一起。

$$
\begin{array}{cc}
\mathrm{Bad} & \mathrm{Better} \\
\hline \\
\iiint_V f(x){\rm d}z {\rm d}y {\rm d}x & \iiint_V f(x)\,{\rm d}z\,{\rm d}y\,{\rm d}x
\end{array}
$$

