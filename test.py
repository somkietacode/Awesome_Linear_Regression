from Awesome_Linear_Regression import linearregression as LR

if __name__ == "__main__" :
  x = np.matrix([[0,1],[1,4],[7,8],[50,23]])
  y = np.matrix([[2],[9],[23],[96]])
  lr = LR(x,y)
  Beta, rss = lr.leastsquare()
  print(Beta)
  print(rss)
  px = np.matrix([[4,7]])
  r_y = lr.predict(px)
  print(r_y)
