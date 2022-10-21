
# Web Scrapping
In this project, information about engineering professors was extracted by crawling into the faculty website. 
## Aim
The aim of this project is to scrape the details of engineering professors from a website and then load it into a dataframe and eventually convert it into a csv file.
## Data Set
As this project involved extraction of information from a website, scrapping was done on the following website URL

https://schulich.ucalgary.ca/electrical-computer/faculty-members
## Process
### Step1:

The project involved creating 3 directories as follows,

#### src
It has a backend directory where webscrap.py file was created. The file consists of all the webscrapping code.

main.py file was created in src directory. This file must be called in order to run the program.
#### data
All results of the running code is stored in this directory.
#### doc
A document consisting of members involved in the project.

### Step2:
A virtual environment was created, and the following packeges were installed in this environment.

    1. pip install beautifulsoup4
    2. pip install requests
    3. pip install pandas
    4. pip install numpy

Versions of each packege used was stored in requirements.txt file.


## Result
The engineering proffesors firstname, lastname, title, homepage, phone number and office were extracted from the above mentioned website url.
The obtained result is as follows,

|    | firstname | lastname      | title               | homepage                                                         | phone_number | office    |
|----|-----------|---------------|---------------------|------------------------------------------------------------------|--------------|-----------|
| 0  | Zahra     | Abbasi        | Assistant Professor | https://profiles.ucalgary.ca/zahra-abbasi                        |              | ICT447    |
| 1  | Hatem     | Abou-Zeid     | Assistant Professor | https://profiles.ucalgary.ca/hatem-abou-zeid                     | 403.220.7151 | ICT252    |
| 2  | Jessica   | Bekker        | Instructor          | https://profiles.ucalgary.ca/jessica-bekker                      |              |           |
| 3  | Mariana   | Bento         | Assistant Professor | https://profiles.ucalgary.ca/mariana-bento                       | 403.220.7073 | ICT251    |
| 4  | Jay       | Carriere      | Assistant Professor | https://profiles.ucalgary.ca/jay-carriere                        |              |           |
| 5  | Steve     | Drew          | Assistant Professor | https://profiles.ucalgary.ca/steve-drew                          | 403.220.7208 | ICT253    |
| 6  | Ignacio   | Galiano       | Assistant Professor | https://profiles.ucalgary.ca/ignacio-galiano-zurbriggen          |              | ICT448    |
| 7  | Yani      | Ioannou       | Assistant Professor | https://profiles.ucalgary.ca/yani-ioannou                        | 403.220.6144 | ICT248    |
| 8  | Hadis     | Karimipour    | Associate Professor | https://profiles.ucalgary.ca/hadis-karimipour                    |              |           |
| 9  | Kangsoo   | Kim           | Assistant Professor | https://profiles.ucalgary.ca/kangsoo-kim                         | 403.220.5644 | ICT247    |
| 10 | Richa     | Pandey        | Assistant Professor | https://profiles.ucalgary.ca/richa-pandey                        |              | ICT255    |
| 11 | Benjamin  | Tan           | Assistant Professor | https://profiles.ucalgary.ca/benjamin-tan                        |              | ICT446    |
| 12 | Ann       | Barcomb       | Assistant Professor | https://schulich.ucalgary.ca/contacts/ann-barcomb                | 403.210.6631 | ICT 352A  |
| 13 | Norm      | Bartley       | Senior Instructor   | https://schulich.ucalgary.ca/contacts/norm-bartley               | 403.220.5060 | ICT 306   |
| 14 | Laleh     | Behjat        | Professor           | https://schulich.ucalgary.ca/contacts/laleh-behjat               | 403.220.8967 | EEEL445A  |
| 15 | Leo       | Belostotski   | Professor           | https://schulich.ucalgary.ca/contacts/leo-belostotski            | 403.210.5426 |           |
| 16 | Laura     | Curiel        | Assistant Professor | https://schulich.ucalgary.ca/contacts/laura-curiel               | 403.220.4390 | ICT346    |
| 17 | Colin     | Dalton        | Assistant Professor | https://schulich.ucalgary.ca/contacts/colin-dalton               | 403.210.8464 | ICT440    |
| 18 | Vassil    | Dimitrov      | Professor           | https://schulich.ucalgary.ca/contacts/vassil-dimitrov            | 403.210.5423 | ICT 443   |
| 19 | Abraham   | Fapojuwo      | Professor           | https://schulich.ucalgary.ca/contacts/abraham-fapojuwo           | 403.220.8524 | ICT 310   |
| 20 | Behrouz   | Far           | Professor           | https://schulich.ucalgary.ca/contacts/behrouz-far                | 403.210.5411 | ICT 541   |
| 21 | Elise     | Fear          | Professor           | https://schulich.ucalgary.ca/contacts/elise-fear                 | 403.210.5413 | ICT 353   |
| 22 | Fadhel    | Ghannouchi    | Professor           | https://schulich.ucalgary.ca/contacts/fadhel-ghannouchi          | 403.220.5807 | ICT 336   |
| 23 | Anis      | Haque         | Teaching Professor  | https://schulich.ucalgary.ca/contacts/anis-haque                 | 403.220.8606 |           |
| 24 | Mohamed   | Helaoui       | Professor           | https://schulich.ucalgary.ca/contacts/mohamed-helaoui            | 403.210.5404 | ICT 340   |
| 25 | Hadi      | Hemmati       | Assistant Professor | https://schulich.ucalgary.ca/contacts/hadi-hemmati               | 403.210.6717 | ICT 309   |
| 26 | Yaoping   | Hu            | Professor           | https://schulich.ucalgary.ca/contacts/yaoping-hu                 | 403.220.4167 | ICT 543   |
| 27 | Seyed     | Jazayeri      | Senior Instructor   | https://schulich.ucalgary.ca/contacts/seyed-pouyan-yani-jazayeri | 403.973.3862 | ICT 344   |
| 28 | Andy      | Knight        | Professor           | https://schulich.ucalgary.ca/contacts/andy-knight                | 403.220.6282 | ICT 454   |
| 29 | Diwakar   | Krishnamurthy | Associate Professor | https://schulich.ucalgary.ca/contacts/diwakar-krishnamurthy      | 403.220.8129 | ICT 535   |
| 30 | Henry     | Leung         | Professor           | https://schulich.ucalgary.ca/contacts/henry-leung                | 403.220.4875 | ICT 451   |
| 31 | Ethan     | MacDonald     | Assistant Professor | https://schulich.ucalgary.ca/contacts/m-ethan-macdonald          | 403.210.6621 | ICT452    |
| 32 | Chris     | Macnab        | Associate Professor | https://schulich.ucalgary.ca/contacts/chris-macnab               | 403.220.4877 | ICT 450   |
| 33 | Emily     | Marasco       | Instructor          | https://schulich.ucalgary.ca/contacts/emily-marasco              | 403.210.6432 | ICT 309   |
| 34 | Brent     | Maundy        | Professor           | https://schulich.ucalgary.ca/contacts/brent-maundy               | 403.220.6177 | ICT 442   |
| 35 | Geoffrey  | Messier       | Professor           | https://schulich.ucalgary.ca/contacts/geoffrey-messier           |              | ICT 308   |
| 36 | Martin    | Mintchev      | Professor           | https://schulich.ucalgary.ca/contacts/martin-p-mintchev          | 403.220.5309 | EN A 121A |
| 37 | Mohammad  | Moshirpour    | Senior Instructor   | https://schulich.ucalgary.ca/contacts/mohammad-moshirpour        | 403.220.6864 | ICT  345  |
| 38 | Mahmood   | Moussavi      | Teaching Professor  | https://schulich.ucalgary.ca/contacts/mahmood-moussavi           | 403.220.6231 | ICT 537   |
| 39 | Kartikeya | Murari        | Associate Professor | https://schulich.ucalgary.ca/contacts/kartikeya-murari           |              | ICT 445   |
| 40 | John      | Nielsen       | Associate Professor | https://schulich.ucalgary.ca/contacts/john-nielsen               | 403.210.9704 | ICT 311   |
| 41 | Steve     | Norman        | Senior Instructor   | https://schulich.ucalgary.ca/contacts/steve-norman               | 403.220.8642 | ICT 411   |
| 42 | Ed        | Nowicki       | Associate Professor | https://schulich.ucalgary.ca/contacts/ed-nowicki                 | 403.220.5006 | ENA 206F  |
| 43 | Anders    | Nygren        | Professor           | https://schulich.ucalgary.ca/contacts/anders-nygren              | 403.220.4192 | ENC 110   |
| 44 | Michal    | Okoniewski    | Professor           | https://schulich.ucalgary.ca/contacts/michal-okoniewski          |              | ICT 354   |
| 45 | Denis     | Onen          | Instructor          | https://schulich.ucalgary.ca/contacts/denis-onen                 | 403.220.4478 | ICT  341  |
| 46 | Yves      | Pauchard      | Instructor          | https://schulich.ucalgary.ca/contacts/yves-pauchard              | 403.210.7416 | ICT246    |
| 47 | Mike      | Potter        | Teaching Professor  | https://schulich.ucalgary.ca/contacts/mike-potter                | 403.220.4129 | ICT 355   |
| 48 | Bill      | Rosehart      | Professor           | https://schulich.ucalgary.ca/contacts/bill-rosehart              |              |           |
| 49 | Guenther  | Ruhe          | Professor           | https://schulich.ucalgary.ca/contacts/guenther-ruhe              | 403.220.7692 | ICT 545   |
| 50 | Abu       | Sesay         | Professor           | https://schulich.ucalgary.ca/contacts/abu-sesay                  | 403.220.6163 | ICT 314   |
| 51 | Michael   | Smith         | Professor           | https://schulich.ucalgary.ca/contacts/michael-smith              | 403.220.6142 | ICT 533   |
| 52 | Roberto   | Souza         | Assistant Professor | https://schulich.ucalgary.ca/contacts/roberto-souza              | 403.210.6544 | ICT 352C  |
| 53 | Gias      | Uddin         | Assistant Professor | https://schulich.ucalgary.ca/contacts/gias-uddin                 | 403.210.6469 | ICT352B   |
| 54 | Rushi     | Vyas          | Assistant Professor | https://schulich.ucalgary.ca/contacts/rushi-vyas                 | 403.220.5002 | ICT 348   |
| 55 | Yingxu    | Wang          | Professor           | https://schulich.ucalgary.ca/contacts/yingxu-wang                | 403.220.6141 | ICT 539   |
| 56 | David     | Westwick      | Professor           | https://schulich.ucalgary.ca/contacts/david-westwick             | 403.220.5806 | ICT 441   |
| 57 | Orly      | Yadid-Pecht   | Professor           | https://schulich.ucalgary.ca/contacts/orly-yadid-pecht           | 403.220.2516 | ICT 436   |
| 58 | Svetlana  | Yanushkevich  | Professor           | https://schulich.ucalgary.ca/contacts/svetlana-yanushkevich      |              | ICT 343   |
| 59 | Hamidreza | Zareipour     | Professor           | https://schulich.ucalgary.ca/contacts/hamidreza-zareipour        | 403.210.9516 | ICT 444   |