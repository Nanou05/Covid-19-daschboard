# Covid-19-dashboard
This is a simplified Covid19 dashboard developed as part of a school project.
This dashboard was 100% developed using python v. 3.7
## Libraries
### Dash
Dash is a productive Python framework for building web analytic applications.

Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. 
It's particularly suited for anyone who works with data in Python.

Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build an interactive web-based application. 
Dash is simple enough that you can bind a user interface around your Python code in an afternoon.

Dash apps are rendered in the web browser. You can deploy your apps to servers and then share them through URLs. 
Since Dash apps are viewed in the web browser, Dash is inherently cross-platform and mobile ready.
The dash library was used throughout the creation of the dashboard. More precisely, the dash.bootstrap.component library was used to produce all the maps with the epidemic monitoring indicators.
 It was also used for its themes in order to give the dashboard the design it has(dbc.themes.BOOTSTRAP).
Dash version: 
*Documentation* : https://dash.plotly.com/introduction 
### Plotly
The plotly.express library was used for the realization of all the graphical visualizations of the dashboard, whether they are dynamic or not.
From this library, several types of charts were used such as bar charts or even line charts. These types of graphs were used because they made it possible to better represent all the data used in the dashboard.

## Data
### World data
For global information on the whole world, the WHO database (which can be downloaded via the link: https://covid19.who.int/WHO-COVID-19-global-data.csv) has been used in particular to calculate global indicators such as the number of cases or deaths. This database contains all the information for all countries and is updated every day, which allows indicators to be updated in real time.
It was also used to produce the dynamic visualizations present in this part, which allows regular updating of information.
For information about vaccination, another WHO database was used (which can be downloaded from the link: https://covid19.who.int/who-data/vaccination-data. csv). This database is updated regularly according to the countries which transmit the information as often as possible.

### French data
For each database presented, the download link is given, all of which are available in open source.
- https://www.data.gouv.fr/fr/datasets/r/6fadff46-9efd-4c53-942a-54aca783c30c: Used for hospital data, it is available in open source.
It contains information on the date, departments, hospitalizations,  ICU admissions, deaths or returns home of patients.
It was used in the dashboard to calculate, in particular, the indicators for the "global view of the situation in France", "resuscitation" and "deaths" pages.
- https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7: Used to obtain the total number of deaths (not only in the hospital environment).
It contains information on departments, sexes, hospitalizations,  ICU admissions, deaths or returns home.
It was used to calculate, in particular, indicators related to the sex ratio in terms of the number of deaths or  ICU admissions.
- https://www.data.gouv.fr/fr/datasets/r/b8d4eb4c-d0ae-4af6-bb23-0e39f70262bd: Used to study the vaccination situation in France.
It contains the information of the different vaccines concerning the number of vaccinations by the first dose and the second dose.
Small database but containing a certain amount of information on the different vaccines prescribed in the first and second dose.
- https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7: Used for the "resuscitation" part and the "death" part of the dashboard targeted on France.
It contains information on the department, gender, date,  ICU admissions, hospitalizations, deaths and returns home.
It was used for the realization of visualizations of  ICU admissions according to time, sex and department.
It was also used for the same visualizations regarding deaths.
It was also used for the realization of the dynamic graphics of the global page of France.
- https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3: Also used in the "resuscitation" part and the "death" part of the dashboard.
It contains information on the region, age group, date, resuscitations, hospitalizations, deaths and returns home.
It was used to carry out visualizations of resuscitation according to age groups and regions.
It was also used for the same visualization regarding deaths.
It was also used for the realization of the dynamic graphics of the global page of France.
- https://www.data.gouv.fr/fr/datasets/r/900da9b0-8987-4ba7-b117-7aea0e53f530: Used in the "vaccination" part of the dashboard targeting France.
It contains information about the region, vaccine type, date, number of doses 1, number of doses 2, cumulative number of doses 1 and cumulative number of doses 2.
It was used for the realization of visualizations concerning the number of doses 1 and 2 per day during the whole period of the pandemic, the evolution of the number of doses 1 and 2 over time.
- https://www.data.gouv.fr/fr/datasets/r/54dd5f8d-1e2e-4ccb-8fb8-eac68245befd: Also used in the "vaccination" part of the dashboard.
It contains information on the age group, the date, the number of doses 1 and the number of complete vaccinations.
It was used to visualize the number of vaccinations according to the age group.
- https://www.data.gouv.fr/fr/datasets/r/735b0df8-51b4-4dd2-8a2d-8e46d77d60d8: Also used in the "vaccination" part of the dashboard.
It contains information about the region, the date, the number of doses 1 and the number of complete vaccinations.
It was used to visualize the number of vaccinations according to the regions.

## Dashboard
The purpose of the dashboard is to monitor indicators of the COVID-19 epidemic around the world and more specifically in France. It has been broken down into 5 distinct parts allowing a more or less precise analysis of the epidemic. For all the visualizations presented in the dashboard, it is possible to select an area to zoom in and double click on the graph to return it to its normal position. Hovering the mouse over the graph also provides more precise information on the selected point.

### World
This page contains 5 epidemic indicator cards:
- Total number of cases
- Total number of deaths
- Total number of vaccinations
- Number of cases of the day (on the date indicated)
- Number of deaths on the day (on the date indicated)
![Capture d’écran 2021-05-15 à 20 40 42](https://user-images.githubusercontent.com/83781622/118374688-d4e29e80-b5bd-11eb-9a5e-365a6b117975.png)

Dynamic visualizations:
![Capture d’écran 2021-05-15 à 20 43 49](https://user-images.githubusercontent.com/83781622/118374807-43276100-b5be-11eb-81d3-944394a9e4bd.png)
![Capture d’écran 2021-05-15 à 20 44 07](https://user-images.githubusercontent.com/83781622/118374836-4de1f600-b5be-11eb-808d-72a2eaa33a1e.png)
This makes it possible to compare the number of new cases over time in two different countries. To do this, it suffices for each of the two graphs to choose the countries that you want to compare from the drop-down menu containing the list.

![Capture d’écran 2021-05-15 à 20 46 11](https://user-images.githubusercontent.com/83781622/118374894-97cadc00-b5be-11eb-8a80-8703c1e15b92.png)
![Capture d’écran 2021-05-15 à 20 46 36](https://user-images.githubusercontent.com/83781622/118374909-a6b18e80-b5be-11eb-8058-990b0b44b55c.png)
This makes it possible to compare the number of new deaths over time in two different countries. To do this, it suffices for each of the two graphs to choose the countries that you want to compare from the drop-down menu containing the list.

![Capture d’écran 2021-05-15 à 23 32 45](https://user-images.githubusercontent.com/83781622/118378706-dc15a680-b5d5-11eb-8f83-8bb93a95d499.png)
![Capture d’écran 2021-05-15 à 23 36 10](https://user-images.githubusercontent.com/83781622/118378800-57775800-b5d6-11eb-939f-f7b01ce3bd1b.png)
These visualizations make it possible to study the evolution of the number of new cases or new deaths in the world with a slider allowing to move the period over which one wishes to study the graph.

![Capture d’écran 2021-05-15 à 23 33 00](https://user-images.githubusercontent.com/83781622/118378712-e637a500-b5d5-11eb-8f51-7a1a66c0e3b2.png)
![Capture d’écran 2021-05-15 à 23 36 40](https://user-images.githubusercontent.com/83781622/118378815-6a8a2800-b5d6-11eb-8ada-a98b92e4e74d.png)
These bar charts allow to study the total number of cases by region in the world, it is possible via the side checklist to remove regions of the world from the chart.

![Capture d’écran 2021-05-15 à 23 37 36](https://user-images.githubusercontent.com/83781622/118378835-8b527d80-b5d6-11eb-9d47-ba8899e4ac8f.png)
This visualization makes it possible to study the number of vaccinations in the world according to the country. The regions of the world are selectable from the side checklist. The linked countries are removed or added to the chart accordingly.

Data Table : 
![Capture d’écran 2021-05-15 à 23 31 20](https://user-images.githubusercontent.com/83781622/118378675-a96bae00-b5d5-11eb-8294-165eeec184c6.png)
This table represents all the data of the world used in particular to carry out the visualizations.
It is possible to apply a filter to each of the columns of this table.
This makes it possible to obtain precise information if one wishes to know the number of cases on a specific date in a given country for example.

### France
This page contains 4 indicator cards:
- The number of total and hospital deaths
- The total number of  ICU admissions
- The total number of hospitalizations
- The total number of complete vaccinations
![Capture d’écran 2021-05-15 à 20 50 02](https://user-images.githubusercontent.com/83781622/118374998-20497c80-b5bf-11eb-9aa9-b04362750d08.png)

Dynamic visualizations:
At the beginning :
![Capture d’écran 2021-05-15 à 20 51 21](https://user-images.githubusercontent.com/83781622/118375020-4ff88480-b5bf-11eb-93d7-0f8c9adf7c23.png)
This visualization makes it possible to study the daily number of resuscitation over time according to the departments chosen in the side checklist. This allows you to study a department or compare several departments with each other.
By default all departments are selected and appear on the graph.
After selection:
![Capture d’écran 2021-05-15 à 20 50 44](https://user-images.githubusercontent.com/83781622/118375007-39eac400-b5bf-11eb-8b81-87e48b2ab9c5.png)
A double click on the list allows you to remove all the departments and to select only those which interest the users.

At the beginning :
![Capture d’écran 2021-05-15 à 20 59 11](https://user-images.githubusercontent.com/83781622/118375195-681cd380-b5c0-11eb-92d8-5bef85b52dcd.png)
Cette visualisation permet d'étudier l'évolution du nombre de décès selon les départements de la même manière que précédemment. 
Par défaut tous les départements sont sélectionnés et apparaissent sur le graphique.
After selection:
![Capture d’écran 2021-05-15 à 21 00 13](https://user-images.githubusercontent.com/83781622/118375209-8da9dd00-b5c0-11eb-85a8-957ba2089c20.png)

Dropdown menu :
![Capture d’écran 2021-05-15 à 21 02 21](https://user-images.githubusercontent.com/83781622/118375244-d9f51d00-b5c0-11eb-9402-78b82e7022be.png)
The drop-down menu allows you to filter the data according to the chosen gender, it offers 3 choices which are reflected in the following graphs.
Graphics:
![Capture d’écran 2021-05-15 à 21 01 55](https://user-images.githubusercontent.com/83781622/118375236-c9dd3d80-b5c0-11eb-8ee8-ed7116204eb6.png)
They update according to the gender chosen in the drop-down menu. They make it possible to study the number of resuscitations and the number of deaths over time according to the sexes.

Dropdown menu :
![Capture d’écran 2021-05-15 à 21 24 07](https://user-images.githubusercontent.com/83781622/118375740-e464e600-b5c3-11eb-8b81-a14f537e46f3.png)
The two drop-down menus allow you to select the two regions that you want to compare in relation to the number of resuscitations over time.![Capture d’écran 2021-05-15 à 21 23 46](https://user-images.githubusercontent.com/83781622/118375734-d7e08d80-b5c3-11eb-8011-40d37807708e.png)
These same graphs are present a second time in this part but with death and not resuscitation as a variable.

#### France  ICU admissions
This page contains 4 indicator cards concerning resuscitation in France with:
- The number of resuscitations in total
- The number of current resuscitations in men
- the number of current resuscitations in women
- The number of new resuscitations
![Capture d’écran 2021-05-15 à 21 28 27](https://user-images.githubusercontent.com/83781622/118375816-7ec52980-b5c4-11eb-9157-9aa97bc704c6.png)

Graphic visualizations:

Study of the number of  ICU admissions as a function of time:
![Capture d’écran 2021-05-15 à 21 33 49](https://user-images.githubusercontent.com/83781622/118375933-3f4b0d00-b5c5-11eb-87f5-1e2f2f8ba488.png)

Study of the number of  ICU admissions according to sex:
![Capture d’écran 2021-05-15 à 21 34 06](https://user-images.githubusercontent.com/83781622/118375938-496d0b80-b5c5-11eb-8206-7ae449d893ef.png)

Study of the number of resuscitations according to the age group:
![Capture d’écran 2021-05-15 à 21 34 19](https://user-images.githubusercontent.com/83781622/118375944-50941980-b5c5-11eb-9519-7551d00bf223.png)

Study of the number of  ICU admissions according to the regions:
![Capture d’écran 2021-05-15 à 21 34 34](https://user-images.githubusercontent.com/83781622/118375947-5a1d8180-b5c5-11eb-895a-ff72a60b3444.png)

Study of the number of ICU admissions according to the departments:
![Capture d’écran 2021-05-15 à 21 34 51](https://user-images.githubusercontent.com/83781622/118375951-63a6e980-b5c5-11eb-9025-2ebb75d6e3f3.png)

#### France Death
This part contains 4 indicator cards concerning deaths in France with:
- The number of total and hospital deaths
- The number of deaths among men in hospitals
- The number of deaths among women in hospitals
- Number of deaths on the day (on the date indicated)
![Capture d’écran 2021-05-15 à 21 33 28](https://user-images.githubusercontent.com/83781622/118375927-33f7e180-b5c5-11eb-8a2a-f70ecae5b216.png)

Graphic visualizations:

Study of the total number of deaths in hospitals as a function of time:
![Capture d’écran 2021-05-15 à 21 38 03](https://user-images.githubusercontent.com/83781622/118376037-d617c980-b5c5-11eb-97f7-20043fe1fba1.png)

Study of the total number of deaths in hospitals according to sex:
![Capture d’écran 2021-05-15 à 21 38 38](https://user-images.githubusercontent.com/83781622/118376050-ec258a00-b5c5-11eb-96f1-7b4711420834.png)

Study of the total number of deaths in hospitals according to age group:
![Capture d’écran 2021-05-15 à 21 38 52](https://user-images.githubusercontent.com/83781622/118376058-f34c9800-b5c5-11eb-9cf4-4778d21a72c4.png)

Study of the total number of deaths by region:
![Capture d’écran 2021-05-15 à 21 39 41](https://user-images.githubusercontent.com/83781622/118376073-10816680-b5c6-11eb-994a-8543f6a354ec.png)

Study of the total number of deaths according to the departments:
![Capture d’écran 2021-05-15 à 21 39 56](https://user-images.githubusercontent.com/83781622/118376082-19723800-b5c6-11eb-86d7-3c140ba13ffb.png)


#### France Vaccination
This part contains 8 indicators concerning vaccination in France with:
- The number of first and second doses of the pfizer vaccine
- The number of first and second doses of the moderna vaccine
- The number of first and second doses of the AstraZeneca vaccine
- The number of first and second doses of the Janssen vaccine
![Capture d’écran 2021-05-15 à 21 33 00](https://user-images.githubusercontent.com/83781622/118375921-22aed500-b5c5-11eb-9f0e-d328d9021f44.png)

Graphic visualizations:

Visualisations graphiques : 
Study of the number of vaccinations per first and second dose as a function of time:
![Capture d’écran 2021-05-15 à 21 41 06](https://user-images.githubusercontent.com/83781622/118376108-44f52280-b5c6-11eb-9d1a-c55a868a3d92.png)

Study of the evolution of the number of vaccinations by the first and second dose as a function of time:
![Capture d’écran 2021-05-15 à 21 41 53](https://user-images.githubusercontent.com/83781622/118376122-60602d80-b5c6-11eb-8873-d8c08d1e7071.png)

Study of the number of complete vaccinations according to the age group of patients:
![Capture d’écran 2021-05-15 à 21 42 31](https://user-images.githubusercontent.com/83781622/118376140-766dee00-b5c6-11eb-9271-b988459f695d.png)

Study of the number of complete vaccinations according to the regions:
![Capture d’écran 2021-05-15 à 21 43 22](https://user-images.githubusercontent.com/83781622/118376154-94d3e980-b5c6-11eb-8286-cf533c8e856d.png)


# Modélisation SIR:
Source de ce jeu de données : https://coronavirus.politologue.com - Les données proposées dans ce fichier sont une compilation des données proposées par le CSSE (The Johns Hopkins University) https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
Les données de ce fichier sont celles qui sont produites pour générer les graphiques sur https: //coronavirus.politologue.com
Vous pouvez utiliser ces données sans problème et une référence à https://coronavirus.politologue.com sera appréciable

# Visualisation SIR pour la France 

![IMG_1671](https://user-images.githubusercontent.com/71569446/118393415-4f073780-b63f-11eb-814e-ab1e73d29e3f.PNG)
![IMG_1673](https://user-images.githubusercontent.com/71569446/118393417-52022800-b63f-11eb-8ff1-d57af3041ad4.PNG)
![IMG_1672](https://user-images.githubusercontent.com/71569446/118393418-53cbeb80-b63f-11eb-99a5-3b0529e8f2dd.PNG)

Dans les 3 visualisations précédentes, nous constatons que le nombre d'infections diminue au cours du temps. Les nombres de guerisons et de déces diminuent également. 


# Visualisation on SIR par pays 

![IMG_1674](https://user-images.githubusercontent.com/71569446/118393460-9db4d180-b63f-11eb-8cc6-97ae6b244101.PNG)

![IMG_1675](https://user-images.githubusercontent.com/71569446/118393480-b0c7a180-b63f-11eb-8b73-986a966fa4da.PNG)

![IMG_1676](https://user-images.githubusercontent.com/71569446/118393482-b58c5580-b63f-11eb-8b6d-e74e6200affc.PNG)


