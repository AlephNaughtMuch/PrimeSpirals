import math
from string import Template

points_data = []

# SET THE LIMIT HERE !!!
# SEE X and Y axis in script to change axis min/max values
limit = 5_000_000

points_data.append([2 * math.cos(2), 2 * math.sin(2)])
points_data.append([3 * math.cos(3), 3 * math.sin(3)])

sieve = [False] * (limit + 1)
for x in range(1, int(math.sqrt(limit)) + 1):
    for y in range(1, int(math.sqrt(limit)) + 1):
        n = 4 * x ** 2 + y ** 2
        if n <= limit and (n % 12 == 1 or n % 12 == 5): sieve[n] = not sieve[n]
        n = 3 * x ** 2 + y ** 2
        if n <= limit and n % 12 == 7: sieve[n] = not sieve[n]
        n = 3 * x ** 2 - y ** 2
        if x > y and n <= limit and n % 12 == 11: sieve[n] = not sieve[n]
for x in range(5, int(math.sqrt(limit))):
    if sieve[x]:
        for y in range(x ** 2, limit + 1, x ** 2):
            sieve[y] = False
for p in range(5, limit):
    if sieve[p]:
        points_data.append([p * math.cos(p), p * math.sin(p)])

# points_data.append([a * math.cos(a), a * math.sin(a)])

html_string = Template("""<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
       google.charts.load('current', {
        'packages': ['corechart']
      });
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['', ''],
          $data
        ]);

        var options = {
          title: 'Prime Points Plot',
          pointSize:0.3,
          colors:['#d113d1'],
          hAxis: {
            minValue: -5000000,
            maxValue: 5000000,
            gridlines: {
                color: 'transparent'
            }
          },
          vAxis: {
            minValue: -5000000,
            maxValue: 5000000,
             gridlines: {
                color: 'transparent'
            }
          },
          legend: 'none',
          backgroundColor: '#000000',
          explorer: {
            keepInBounds: true,
            maxZoomIn: 10000.0
          }
        };

        var my_div = document.getElementById('chart_div');
        var my_chart = new google.visualization.ScatterChart(chart_div);

        my_chart.draw(data, options);
      }
</script>
</head>
<body>
    <div id="chart_div" style="width:1400; height:1400"></div>
</body>
</html>""")

chart_data_str = ''
for row in points_data:
    chart_data_str += '%s,\n' % row

completed_html = html_string.substitute(data=chart_data_str)

with open('prime_spiral_chart.html', 'w') as file:
    file.write(completed_html)