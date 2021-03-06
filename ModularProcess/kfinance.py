import pandas as pd
import mplfinance as mpf

rawData = [[
    '2022-05-23', '17.60', '17.48', '0.24', '1.39%', '17.24', '18.00',
    '434111', '76404.02', '2.76%'
],
           [
               '2022-05-20', '16.75', '17.24', '0.70', '4.23%', '16.75',
               '17.69', '325648', '56251.07', '2.07%'
           ],
           [
               '2022-05-19', '16.45', '16.54', '-0.12', '-0.72%', '16.15',
               '16.58', '154983', '25338.99', '0.99%'
           ],
           [
               '2022-05-18', '16.57', '16.66', '0.27', '1.65%', '16.39',
               '16.96', '176880', '29632.92', '1.13%'
           ],
           [
               '2022-05-17', '16.69', '16.39', '-0.28', '-1.68%', '16.20',
               '16.70', '149722', '24502.75', '0.95%'
           ],
           [
               '2022-05-16', '17.00', '16.67', '-0.27', '-1.59%', '16.55',
               '17.20', '160210', '26958.68', '1.02%'
           ],
           [
               '2022-05-13', '17.15', '16.94', '-0.11', '-0.65%', '16.71',
               '17.42', '138557', '23484.64', '0.88%'
           ],
           [
               '2022-05-12', '16.80', '17.05', '0.06', '0.35%', '16.71',
               '17.20', '135937', '23119.73', '0.86%'
           ],
           [
               '2022-05-11', '16.87', '16.99', '0.16', '0.95%', '16.87',
               '17.36', '206529', '35491.68', '1.31%'
           ],
           [
               '2022-05-10', '16.75', '16.83', '-0.07', '-0.41%', '16.56',
               '16.93', '141534', '23722.62', '0.90%'
           ],
           [
               '2022-05-09', '16.67', '16.90', '0.16', '0.96%', '16.61',
               '17.02', '117038', '19737.30', '0.74%'
           ],
           [
               '2022-05-06', '16.64', '16.74', '-0.30', '-1.76%', '16.56',
               '16.93', '126684', '21205.14', '0.80%'
           ],
           [
               '2022-05-05', '16.71', '17.04', '0.35', '2.10%', '16.41',
               '17.21', '232625', '39465.68', '1.48%'
           ],
           [
               '2022-04-29', '16.00', '16.69', '1.15', '7.40%', '15.87',
               '16.75', '290004', '47663.23', '1.84%'
           ],
           [
               '2022-04-28', '15.84', '15.54', '-0.37', '-2.33%', '15.35',
               '15.96', '208491', '32599.30', '1.32%'
           ],
           [
               '2022-04-27', '15.42', '15.91', '0.27', '1.73%', '15.01',
               '15.91', '265236', '41076.20', '1.68%'
           ],
           [
               '2022-04-26', '16.00', '15.64', '-0.17', '-1.08%', '15.61',
               '16.15', '208594', '33150.75', '1.33%'
           ],
           [
               '2022-04-25', '16.60', '15.81', '-1.13', '-6.67%', '15.81',
               '16.78', '239837', '39075.34', '1.52%'
           ],
           [
               '2022-04-22', '16.99', '16.94', '-0.23', '-1.34%', '16.68',
               '17.23', '159774', '27087.71', '1.02%'
           ],
           [
               '2022-04-21', '17.65', '17.17', '-0.53', '-2.99%', '17.11',
               '17.82', '223076', '38968.26', '1.42%'
           ],
           [
               '2022-04-20', '17.74', '17.70', '-0.22', '-1.23%', '17.61',
               '18.22', '268166', '48010.47', '1.70%'
           ],
           [
               '2022-04-19', '18.50', '17.92', '-0.61', '-3.29%', '17.73',
               '18.59', '274500', '49505.52', '1.74%'
           ],
           [
               '2022-04-18', '18.47', '18.53', '-0.02', '-0.11%', '18.08',
               '18.80', '119574', '21994.12', '0.76%'
           ],
           [
               '2022-04-15', '18.45', '18.55', '0.02', '0.11%', '18.35',
               '18.75', '103659', '19243.79', '0.66%'
           ],
           [
               '2022-04-14', '18.40', '18.53', '0.19', '1.04%', '18.40',
               '18.71', '113566', '21075.82', '0.72%'
           ],
           [
               '2022-04-13', '18.85', '18.34', '-0.64', '-3.37%', '18.34',
               '18.85', '138923', '25780.56', '0.88%'
           ],
           [
               '2022-04-12', '18.68', '18.98', '0.24', '1.28%', '18.38',
               '19.02', '154463', '28918.37', '0.98%'
           ],
           [
               '2022-04-11', '19.18', '18.74', '-0.71', '-3.65%', '18.61',
               '19.28', '213119', '40235.43', '1.35%'
           ],
           [
               '2022-04-08', '19.65', '19.45', '-0.20', '-1.02%', '19.12',
               '19.77', '185583', '36026.88', '1.18%'
           ],
           [
               '2022-04-07', '20.15', '19.65', '-0.56', '-2.77%', '19.64',
               '20.31', '209045', '41608.61', '1.33%'
           ]]

data = [(i[1:3] + i[5:8]) for i in rawData]
dataNumber = []
for line in data:
    # print(line)
    dataNumber.append([float(x) for x in line])
print(dataNumber)
index = [i[0] for i in rawData]
index = pd.DatetimeIndex(index)

columns = ['Open', 'Close', 'Low', 'High', 'Volume']
daily = pd.DataFrame(dataNumber, columns=columns, index=index)
daily.index.name = 'Date'

print(daily)

# mpf.plot(daily)
mpf.plot(daily,
         type='candle',
         mav=(3, 6, 9),
         volume=True,
        #  savefig=dict(fname='KOsmall',dpi=60)
         )
