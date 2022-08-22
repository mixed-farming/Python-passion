from sklearn.linear_model import LinearRegression as lr

reg=lr()

X=[[1],[2],[3],[4],[5],[6]]
Y=[2,4.25,6.88,9,9,12] #Y~2X

reg.fit(X,Y)

print(reg.predict([[7]]))

"""
Here lr() is a class(of objects)
reg is an instance in the lr class
predict(),fit() are the methods of the lr class
"""
