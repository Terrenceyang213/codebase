%%#######################################################
q_left_up=[
    [3,2,1]
    [2,2,0]
    [1,0,1]
]
inv(q_left_up)
%    1.0e+15 *
% 
%     3.8602   -3.8602   -3.8602
%    -3.8602    3.8602    3.8602
%    -3.8602    3.8602    3.8602

inv(q_left_up)*q_left_up
%      1     0     0
%      0     1     0
%      0     0     1

%%
q_left_down =[
    [1,0,1]
    [2,2,0]
    [3,2,1]
]
inv(q_left_down)
%    1.0e+15 *
% 
%    -3.8602   -3.8602    3.8602
%     3.8602    3.8602   -3.8602
%     3.8602    3.8602   -3.8602

inv(q_left_down)*q_left_down
%     0.5000    1.0000    0.5000
%    -0.5000         0   -0.5000
%     1.0000         0    1.0000

%%
q_right_up = [
    [1,2,3]
    [0,2,2]
    [1,0,1]
]

inv(q_right_up)
%    Inf   Inf   Inf
%    Inf   Inf   Inf
%    Inf   Inf   Inf

inv(q_right_up)*q_right_up

%    NaN   NaN   Inf
%    NaN   NaN   Inf
%    NaN   NaN   Inf

%%
q_right_down = [
    [1,0,1]
    [0,2,2]
    [1,2,3]
]

inv(q_right_down)
%    Inf   Inf   Inf
%    Inf   Inf   Inf
%    Inf   Inf   Inf

inv(q_right_down)*q_right_down
%    NaN   NaN   Inf
%    NaN   NaN   Inf
%    NaN   NaN   Inf