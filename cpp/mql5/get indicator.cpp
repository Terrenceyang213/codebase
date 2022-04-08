
double maVal[]; // 保存每个柱移动平均值的动态数组
ArraySetAsSeries(maVal,true); //把索引倒排

int maHandle;  // 我们移动平均指标的句柄


//--- 得到移动平均指标的句柄
maHandle=iMA(_Symbol,_Period,MA_Period,0,MODE_EMA,PRICE_CLOSE);

//--- 如果句柄返回了无效句柄
if(maHandle<0)
{
    Alert("创建指标句柄出错 - 错误: ",GetLastError(),"!!");
}

// 将句柄指向的指标复制3期数据到maVal
if(CopyBuffer(maHandle,0,0,3,maVal)<0)
{
    Alert("复制移动平均指标缓冲区出错 - 错误:",GetLastError());
    return;
}