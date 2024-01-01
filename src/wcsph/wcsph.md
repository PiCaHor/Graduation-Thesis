核函数
$$
W(r,h) =\sigma_d \begin{cases}
6(q^3-q^2) + 1 & 0\leq q \leq0.5 \\
2(1-q)^3 & 0.5\leq q \leq1 \\
0 & otherwise
\end{cases} \\
with \ q ={||r|| \over h} 
\ \ \ \   \sigma_1={4 \over3h} 
\ \ \ \   \sigma_2={40 \over7{\pi}h^2}  
\ \ \ \   \sigma_3={8 \over{\pi}h^3}
$$
核函数导数
$$
\nabla W(r,h) =\sigma_d \begin{cases}
(3q^2-2q) * {r \over ||r|| * h} & 0\leq q \leq0.5 \\
-(1-q)^2 *  {r \over ||r|| * h} & 0.5\leq q \leq1 \\
0 & otherwise
\end{cases} \\
with \ q ={||r|| \over h} 
\ \ \ \   \sigma_1={24 \over3h} 
\ \ \ \   \sigma_2={240 \over7{\pi}h^2}  
\ \ \ \   \sigma_3={48 \over{\pi}h^3}
$$


速度场拉普拉斯算子

代码公式：

有限差分方法

来自论文： 

Monaghan J J. Smoothed particle hydrodynamics[J]. Reports on progress in physics, 2005, 68(8): 1703-1759
$$
\nabla^2v = 2(d+2) {\sum}{m_j \over \rho_j}{(v_{ij} * x_{ij})\over ||x_{ij}||^2 + 0.01h^2} \nabla W_{ij}\\
where \ v_{ij} = (v_i - v_j).dot(||x_{ij}||)
$$
原sph公式： 反对称
$$
\nabla^2v = {\sum}{m_j }{(v_j - v_i)\over \rho_j} \nabla^2 W_{ij}
$$


压力场:对称式
$$
p_i = k_1(({\rho_1\over\rho_0})^{k_2} - 1) \\
{1 \over \rho_i } \nabla p_i = \sum_{j=0} ^ {n} m_j({p_i \over\rho_i^2} + {p_j \over\rho_j^2})  \nabla W_{ij}
$$

