import matplotlib.pyplot as pyplot
pyplot.plot([ "Jan." , "Fev ." , "Mar ." , "A br . " , "Maio" , "Jun . " , "Jul . " , "Ago . " ,"Set.", "Out." , " Nov." , " Dez."],[9.03,9.78,12.37,13.99,16.78,20.39, 22.54, 22.92, 20.48, 16.84, 12.28, 9.75], '-o' , color= " purple ",linewidth=3)
pyplot.title( ' Temperatura Média 1991-2019(Portugal Continental - Fonte IPMA) ' )
pyplot.ylabel( 'Temperatura ( º C) ' )
pyplot.xlabel ('Mês')
pyplot.grid ()
pyplot.show()