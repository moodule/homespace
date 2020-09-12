####
TODO
####

******
GLOBAL
******

- [x] replace the '-' in the package name
- [x] move the wrangling scripts into the data folder
- [x] use poetry for dep management, instead of pipenv
- [x] move the scraping scripts into the data folder
- [x] keep only the modules in adspying
- [ ] move the serialized data out of the project
- [ ] save all the data in mongodb
- [ ] move relevant sections to README (workflow, overall steps)
- [ ] put all the initiation steps on a jupyter notebook
- [ ] create a dashboard in dash / bokeh
- [ ] move the referential in the python package
- [ ] init script / notebook

*******
WORFLOW
*******

- [ ] collect / update referentials
- [ ] collect / update ads
- [ ] define project
- [ ] rate & rank ads
- [ ] view the ads : select the relevant offers, refine project
- [ ] complete the data (call the sellers, correct the data errors)
- [ ] buy the perfect van !

*******************
STEPS TO VANLIFE :)
*******************

- [x] data collection
- [x] data cleaning & merging
- [x] ad scraping & alerts
- [ ] filtering & ranking tools
- [ ] project dashboard
- [ ] sharing datasets : kaggle, open datasets => loop back on gh
- [ ] contact, verification of ads
- [ ] & finally buying ! and begining a new chapter !..
- [ ] diy conversion : electricity, internet, solar, water, bedding, furniture, insulation
- [ ] stacking money

***************
DATA COLLECTION
***************

- [ ] replace the datasets with a download script, in the repo
- [ ] car (especially van) size (volume)
- [ ] car lifespan
- [ ] fuel costs per region (country most likely)
- [x] van mpg & emissions
- [ ] insurance prices database / scraping
- [x] van / utility list
- [ ] repairs costs
- [ ] conversion costs
- [ ] parking costs

************
ADS SCRAPING
************

- [x] referential :
  - [x] regions
  - [x] cities
  - [x] ad categories
  - [x] url formats by categories => parameters dict (cat => param => url parts)
  - [x] xpath to data
- [x] configure search : date, max price, min & max years, mileage
- [x] extract informations :
  - [x] by fixing filtering input (location, price etc)
  - [x] by scraping the html
    - [x] manufacturer
    - [ ] model
    - [x] location
    - [x] price
    - [x] mileage
    - [ ] contact
    - [x] ad age
    - [ ] ad update count
- [ ] fill the gaps by asking the seller

*********
WRANGLING
*********

- [ ] filter out the cars & trucks : keep only vans ?
- [ ] list all vans & utilities
- [ ] remove the samples with 0 / NULL data
- [x] swap the mpg / lpkm confusion errors
- [ ] switch the metric / imperial measures when there's a mistake

*******
MERGING
*******

- [x] define the headers
- [ ] common units
- [ ] merge consumption / size
- [ ] merge ads with referential (complete the ad infos)
- [ ] put unrecognized ads in a separate file

*******
DATAVIZ
*******

- [ ] plot the ad price vs most characteristics
- [ ] plot the averages / stds

******
MINING
******

- [x] plot consumption vs emission (by fuel type)
- [x] linear regression :
  - [x] mpg vs emission vs fuel type
  - [ ] mpg vs (gross) weight
- [x] estimation from combustion chemistry

*************
CAR VALUATION
*************

- [ ] age & mileage
- [ ] fuel efficiency / current models
- [ ] reparation cost
- [ ] conversion cost
- [ ] equipment cost
- [ ] actual cost (price_new + all)
- [ ] fuel & electricity price
- [ ] cost at 0 & 100 000 km

*******
RANKING
*******

- [ ] normalize each column used for rating
- [ ] metric for fuel consumption
- [ ] metric for co2, co, nox, pm emissions
- [ ] metric for habitable space
- [ ] metric for mileage
- [ ] metric for the cost
- [ ] overall priority for each metric
- [ ] global rating
- [ ] rank all the potential vehicles
- [ ] rank all the ads

*******
HONESTY
*******

- [ ] compare the informations from the seller to the ref
- [ ] détails et contenu de l'annonce (déjà la taille...)
- [ ] ratio estimated value / price

*********
DASHBOARD
*********

- [ ] Project :
  - [ ] habitable space : min x, y, z, V
  - [ ] budget : fuel, diy, van, insurance
  - [ ] miles / months, year, total
  - [ ] priorities (relative weights) : price, space, (mile)age,
  - [ ] ranges : consumption (from budget vs miles)
- [ ] Reparation costs :
  - [ ] MOT
  - [ ] paint
  - [ ] tyres
  - [ ] mech ?
- [ ] Conversion costs :
  - [ ] materials
  - [ ] insulation
  - [ ] water tank
  - [ ] batteries
  - [ ] solar panels ?
  - [ ] tools
  - [ ] garage
- [ ] Living costs :
  - [ ] electricity : kW/h
  - [ ] diesel
  - [ ] petrol
  - [ ] lpg
  - [ ] insurance
  - [ ] parking (% time idle)
  - [ ] total (over a period / distance)
- [ ] rank & highlight ads

************
VERIFICATION
************

- [ ] mileage
- [ ] technical checkup
- [ ] papers

**************
DIY CONVERSION
**************

- [ ] cost of diy materials / tools / etc
- [ ] planning & tracking of the conversion
- [ ] satellite dish => internet connection

****
TEST
****

- [ ] find model & make
- [ ] find closest make
