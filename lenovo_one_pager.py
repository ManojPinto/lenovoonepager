"""
Lenovo Knowledge Vault - IT Helpdesk Home
==========================================
Streamlit app — single file, zero extra dependencies beyond streamlit.

Usage:
    streamlit run lenovo_one_pager.py
"""

import streamlit as st
import streamlit.components.v1 as components

# ── Allowed users: email (lowercase) → display name ────────────────────────
ALLOWED_USERS = {
    'aabdulrawoof@lenovo.com': 'Afridh Abdulrawoof',
    'aabhiram@lenovo.com': 'P Abhiram',
    'aafrid@lenovo.com': 'A AFRID',
    'aahammed@lenovo.com': 'Aman Ahammed',
    'aahmed3@lenovo.com': 'Aqeeb Ahamed M B',
    'aahmed9@lenovo.com': 'A R Rizwan Ahmed',
    'mpintoo@lenovo.com': 'Manoj Pinto',
    'vraj@lenovo.com': 'Vinil Raj',
    'rmondal2@lenovo.com': 'Ramkrishna Mondal',
    'aaman1@lenovo.com': 'Aman .',
    'aambika@lenovo.com': 'Ambika',
    'aanjum1@lenovo.com': 'Asfiya Anjum',
    'aanthony2@lenovo.com': 'Ananya Anthony',
    'aanusha2@lenovo.com': 'Anusha Anusha',
    'abarbhuiya@lenovo.com': 'Ashfak Hussain Barbhuiya',
    'abasappa@lenovo.com': 'Mr. Anubasappa .',
    'abasha1@lenovo.com': 'Anees Basha',
    'abawaskar@lenovo.com': 'Akansha Bawaskar',
    'abehera@lenovo.com': 'Artatrana Behera',
    'abellad@lenovo.com': 'Amit Bellad',
    'abhange@lenovo.com': 'Anushka',
    'abharadwaj1@lenovo.com': 'Anurag Bharadwaj',
    'abhimawad@lenovo.com': 'ARYAN BHIMAWAD',
    'abhongade@lenovo.com': 'Amol Shioshankar Bhongade',
    'abiswal3@lenovo.com': 'Ankit Biswal',
    'achaggan@lenovo.com': 'Abdul Razak Chaggan',
    'achakrabort4@lenovo.com': 'Archiman Chakraborty',
    'achapparband@lenovo.com': 'Akil Kadarali Chapparband',
    'achoubey2@lenovo.com': 'Arshit Choubey',
    'acv@lenovo.com': 'Andrew William C V',
    'ad1@lenovo.com': 'Akshay Kumar D',
    'adas8@lenovo.com': 'Ayan Das',
    'adas9@lenovo.com': 'Adyasha Das',
    'adey2@lenovo.com': 'Annyasha Dey',
    'aedwin@lenovo.com': 'Akhil Edwin',
    'afathima1@lenovo.com': 'Almas Fathima',
    'afathima3@lenovo.com': 'Ayesha Fathima',
    'mpintoo@lenovo.com': 'Manoj Pinto',
    'vraj@lenovo.com': 'Vinil Raj',
    'rmondal2@lenovo.com': 'Ramkrishna Mondal',
    'afernandez8@lenovo.com': 'Avrel Fernandez',
    'agadagwale@lenovo.com': 'Arpita Gadagwale',
    'agaur@lenovo.com': 'Akash Gaur',
    'ageorge5@lenovo.com': 'Alin Maria George',
    'agiri2@lenovo.com': 'Aishwarya Giri',
    'agoswami4@lenovo.com': 'Arup Goswami',
    'agupta18@lenovo.com': 'Ajay Kumar Gupta',
    'agupta52@lenovo.com': 'Aradhya  Gupta',
    'ah5@lenovo.com': 'Aliya H',
    'ahameed@lenovo.com': 'Abdul Hameed',
    'ahassain@lenovo.com': 'Athika Hassain',
    'ahassan7@lenovo.com': 'Aamir Hassan',
    'ahussain5@lenovo.com': 'Altafhussain Karimsab Tahasildar',
    'aiyoob@lenovo.com': 'A ARSHAD IYOOB',
    'aj4@lenovo.com': 'Abdul Khadar J',
    'ajain27@lenovo.com': 'Aniket Jain',
    'ajain28@lenovo.com': 'Asmita Jain',
    'ajena1@lenovo.com': 'Ajit Kumar Jena',
    'ajoseph@lenovo.com': 'Augustine Joseph',
    'ak13@lenovo.com': 'Ashith K',
    'ak22@lenovo.com': 'ASHRAF UNNISA K',
    'ak4@lenovo.com': 'Amog K',
    'akalra@lenovo.com': 'Ankit Kalra',
    'akarale@lenovo.com': 'Aakash Rajesh Karale',
    'akarthik2@lenovo.com': 'Karthik A',
    'akashyap1@lenovo.com': 'Ashish Kashyap',
    'akhan34@lenovo.com': 'Arbaz Khan',
    'akolkur@lenovo.com': 'Akshay Kolkur',
    'akulkarni8@lenovo.com': 'Akanksha A  Kulkarni',
    'akumar127@lenovo.com': 'ABHISHEK KUMAR',
    'akumar151@lenovo.com': 'Ayush Kumar',
    'akumar152@lenovo.com': 'Animesh Kumar',
    'akumar69@lenovo.com': 'Arun Kumar M',
    'akumar70@lenovo.com': 'Ashish Kumar',
    'akumar72@lenovo.com': 'Aman Kumar',
    'akumar80@lenovo.com': 'Kumar Abhishek',
    'akumar96@lenovo.com': 'AnilKumar Balaraju',
    'al4@lenovo.com': 'H L Adarsh',
    'am25@lenovo.com': 'Athira Nair M',
    'amaidur@lenovo.com': 'Amar Maidur',
    'amandal3@lenovo.com': 'Abhishek Kumar Mandal',
    'amardhekar@lenovo.com': 'Akshay Anil Mardhekar',
    'amishra13@lenovo.com': 'Anuj Mishra',
    'amohammed3@lenovo.com': 'Atheer Mohammed',
    'amr1@lenovo.com': 'Ajith M R',
    'amultani@lenovo.com': 'Ayesha Multani',
    'anaaz@lenovo.com': 'Arshiya Naaz',
    'aojha@lenovo.com': 'Ashis Kumar Ojha',
    'ap15@lenovo.com': 'Arvind Kumar P',
    'ap4@lenovo.com': 'Arnold P',
    'apanda2@lenovo.com': 'Amit panda',
    'apanda5@lenovo.com': 'Adarsh Panda',
    'apandey21@lenovo.com': 'Akansha Pandey',
    'apandey22@lenovo.com': 'Aaddarsh Pandey',
    'apati@lenovo.com': 'Amit Pritam Pati',
    'apatil12@lenovo.com': 'Abhishek Kallappa Patil',
    'apatil13@lenovo.com': 'Akshaykumar S Patil',
    'apatil16@lenovo.com': 'Adithi C Patil',
    'apatode@lenovo.com': 'Anil',
    'apj@lenovo.com': 'Ajin Pj',
    'aporwal@lenovo.com': 'Ankit Porwal',
    'apradhan2@lenovo.com': 'Anulipsa Pradhan',
    'apradhan5@lenovo.com': 'Ajaya Pradhan',
    'aprasad10@lenovo.com': 'Aniket Prasad',
    'apriya1@lenovo.com': 'Annu Priya',
    'ar9@lenovo.com': 'Arvind R',
    'araheem@lenovo.com': 'Abdul Raheem',
    'araj19@lenovo.com': 'Aanchal Raj',
    'arawat2@lenovo.com': 'Avantika Rawat',
    'areddy7@lenovo.com': 'Adimireddy Kumar Reddy',
    'arehman@lenovo.com': 'Abdul Rehman Khan',
    'as25@lenovo.com': 'Alameen S',
    'as26@lenovo.com': 'Aftab Pasha S',
    'as38@lenovo.com': 'Aashu  S',
    'as6@lenovo.com': 'Arul S',
    'asahoo1@lenovo.com': 'Atish Kumar Sahoo',
    'asaini2@lenovo.com': 'Arjun Saini',
    'asarkhel@lenovo.com': 'Abhijeet Sarkhel',
    'asbhat@lenovo.com': 'Anand sbhat',
    'aseet@lenovo.com': 'Ashish  Kumar Seet',
    'ashahi@lenovo.com': 'Adarsh Pratap Shahi',
    'asharma37@lenovo.com': 'ABHILASH KUMAR SHARMA',
    'ashirur@lenovo.com': 'Abdulkhadar Shirur',
    'asingh101@lenovo.com': 'Aniket Kumar Singh',
    'asingh102@lenovo.com': 'Aryan Singh',
    'asingh104@lenovo.com': 'Aman kumar Singh',
    'asingh56@lenovo.com': 'Aanand Kumar',
    'asingh89@lenovo.com': 'Akash Singh',
    'asrivastava3@lenovo.com': 'Ankur Srivastava',
    'asubbaiah@lenovo.com': 'Avula Subbaiah',
    'asultana@lenovo.com': 'Ayesha Sultana M',
    'asuman@lenovo.com': 'Ashutosh Suman',
    'aswami@lenovo.com': 'M Arvind Swami',
    'asyed3@lenovo.com': 'Ali Syed',
    'atalikoti1@lenovo.com': 'Rahila Anjum Mohammed Paigamber Talikoti',
    'atiwari16@lenovo.com': 'Ankit Tiwari',
    'ausama@lenovo.com': 'Abdul Waheed Usama',
    'av10@lenovo.com': 'Akshay N V',
    'av9@lenovo.com': 'Arivazhahan V',
    'avamshi@lenovo.com': 'Andela Vamshi',
    'averma12@lenovo.com': 'Ashwini  Kumar Verma',
    'averma16@lenovo.com': 'Adarsh Umang Verma',
    'avishnu@lenovo.com': 'Ajay Vishnu Sampathkumar',
    'axavier2@lenovo.com': 'Alex Xavier',
    'ayadav19@lenovo.com': 'Anuradha Yadav',
    'ayerimani1@lenovo.com': 'Ayesha M Yerimani',
    'azahid@lenovo.com': 'Adeeb Zahid',
    'baritra@lenovo.com': 'Aritra  Bhattacharjee',
    'bashwini1@lenovo.com': 'Ashwini N Biradar',
    'bbaruah@lenovo.com': 'Banashree Baruah',
    'bbasak@lenovo.com': 'Bapi basak',
    'bbc1@lenovo.com': 'Bindya B C',
    'bbehera1@lenovo.com': 'Biswajit Behera',
    'bbiharidhara@lenovo.com': 'Binod Bihari Dhara',
    'bchabuksawar@lenovo.com': 'Basit M Chabuksawar',
    'bchavan@lenovo.com': 'Bhavana Praveen Chavan',
    'bchettri@lenovo.com': 'Bijay Chettri',
    'bd3@lenovo.com': 'Bharath M D',
    'bdas2@lenovo.com': 'Bishal Das',
    'bgeorge4@lenovo.com': 'Bibin George',
    'bhajira@lenovo.com': 'Bi Bi Hajira',
    'bmuneer@lenovo.com': 'Burhan Muneer',
    'bnikhath@lenovo.com': 'Nikhath Begum',
    'bpatra@lenovo.com': 'Bedabyas Patra',
    'bpatted@lenovo.com': 'Bharati Patted',
    'bsahu@lenovo.com': 'Bhanu Prakash Sahu',
    'bsamal1@lenovo.com': 'Bikash Chandra Samal',
    'bsankar1@lenovo.com': 'Bhabani Sankar Raul',
    'bsen@lenovo.com': 'Bijit Sen',
    'bv6@lenovo.com': 'Bhavana V',
    'bvarma1@lenovo.com': 'BATTINI SANJAY VARMA',
    'cb2@lenovo.com': 'Chandan M B',
    'cb@lenovo.com': 'Chetan B',
    'cdebnath@lenovo.com': 'CHAITY DEBNATH',
    'cg2@lenovo.com': 'Chandrasekar G',
    'chatarki@lenovo.com': 'Chethan C Hatarki',
    'cikhar@lenovo.com': 'Chandrika Sureshravji Ikhar',
    'cmogaveera@lenovo.com': 'Chethan Ramachandra Mogaveera',
    'cpanigrahi@lenovo.com': 'CHIDANANDA PANIGRAHI',
    'cprakash@lenovo.com': 'Chandra Prakash',
    'cprasad1@lenovo.com': 'Chillakuru Prasad',
    'crakha1@lenovo.com': 'Chandan Rakha',
    'cramani@lenovo.com': 'Chahat Pravinbhai Ramani',
    'cs3@lenovo.com': 'Chandana S',
    'cs6@lenovo.com': 'Calidoss',
    'csingh3@lenovo.com': 'Chandra Prakash Singh',
    'csuthar@lenovo.com': 'Chetan Suthar',
    'cyadav@lenovo.com': 'Chandrakesh Yadav',
    'dbabu1@lenovo.com': 'Delhi Babu B',
    'dbharathi1@lenovo.com': 'Divya Bharathi',
    'dbindra@lenovo.com': 'Deepanshu Bindra',
    'ddyamangouda@lenovo.com': 'Deepa S Dyamangoudar',
    'dghosh@lenovo.com': 'Ghosh Deepak Dulalchandra',
    'dgurjar@lenovo.com': 'Dinesh Gurjar',
    'dkumar22@lenovo.com': 'Dinesh Kumar G A',
    'dmalviya2@lenovo.com': 'Dilip Malviya',
    'dmishra6@lenovo.com': 'Dhruv Mishra',
    'dn1@lenovo.com': 'Deepak N',
    'dn5@lenovo.com': 'Dadapeer N',
    'dnagaraj@lenovo.com': 'Nagaraj Dhamlyanayak Lamani',
    'dpadhy@lenovo.com': 'Debasis Padhy',
    'dpanda@lenovo.com': 'Debasish Panda',
    'dpanday@lenovo.com': 'Deepak Kumar Panday',
    'dpanigrahi@lenovo.com': 'Dibyajyoti Panigrahi',
    'dr11@lenovo.com': 'Deekshith S R',
    'drai@lenovo.com': 'Deepisha Rai',
    'draj4@lenovo.com': 'Deepak Raj',
    'ds6@lenovo.com': 'Dinesh S',
    'dsamal1@lenovo.com': 'DEBASMITA SAMAL',
    'dsen1@lenovo.com': 'Disha Sen',
    'dshetty3@lenovo.com': 'Dhanush S Shetty',
    'dswetha@lenovo.com': 'Devapatla Sai Swetha',
    'ebadami@lenovo.com': 'Badami Ethihas',
    'ec1@lenovo.com': 'Emmanuel',
    'ekesarkar@lenovo.com': 'Ekanath Parasharam Kesarkar',
    'emaoreya@lenovo.com': 'Ekta Maoreya',
    'enavagire@lenovo.com': 'Elizabeth K Navagire',
    'eupadhyaya@lenovo.com': 'Eklavya Upadhaya',
    'fahmed3@lenovo.com': 'Faiz Ahmed Chitgi',
    'fahmed6@lenovo.com': 'Faiz Ahmed',
    'fdarvesh@lenovo.com': 'Faisal Ur Rehman Darvesh',
    'fshariff@lenovo.com': 'Fouz Ulla Shariff',
    'fzahura@lenovo.com': 'I K Fathima Zahura',
    'ga2@lenovo.com': 'A R  Gourish',
    'ganand3@lenovo.com': 'Gokul Anand',
    'gankita@lenovo.com': 'Ankita Govindsa Bakale',
    'gd1@lenovo.com': 'Geetha Kumari',
    'ggarnaik@lenovo.com': 'Geetika Garnaik',
    'ghasan@lenovo.com': 'Gulam Hasan',
    'gk11@lenovo.com': 'K Guru Prasad',
    'gkadlaskar@lenovo.com': 'Gautam  Madhukar Kadlaskar',
    'gkondaguli@lenovo.com': 'Gururaj Kondaguli',
    'gkumar19@lenovo.com': 'GOUTAM KUMAR',
    'gmahesh@lenovo.com': 'Gaikwad  Mahesh',
    'greddy2@lenovo.com': 'R Gowtham',
    'grotti@lenovo.com': 'Gopal Rotti',
    'gsingh27@lenovo.com': 'Gaurav Singh',
    'gsudharani@lenovo.com': 'Gurukuntla Sudharani',
    'gv6@lenovo.com': 'Girisha B V',
    'hanand@lenovo.com': 'Harshith A',
    'hbasha1@lenovo.com': 'Hafeez Basha',
    'hbhardwaj@lenovo.com': 'HARSHIT BHARDWAJ',
    'hc4@lenovo.com': 'Husna C',
    'hchandra1@lenovo.com': 'Harikesh Chandra',
    'hdeshmukh@lenovo.com': 'Hitesh Diliprao Deshmukh',
    'hkaliappan@lenovo.com': 'Hari Kaliappan',
    'hkhan3@lenovo.com': 'Hamid Raza Khan',
    'hkhanum@lenovo.com': 'Hifza Khanum',
    'hkm@lenovo.com': 'Harsha Km',
    'hkumar16@lenovo.com': 'M Hari Kumar',
    'hpatel4@lenovo.com': 'HRITIK PATEL',
    'hr1@lenovo.com': 'Hemanth R',
    'hr5@lenovo.com': 'Harini R',
    'hr6@lenovo.com': 'Harshith Singh N R',
    'hrajahamsa@lenovo.com': 'H M Rajahamsa',
    'hrao1@lenovo.com': 'Harshitha H Rao',
    'hs2@lenovo.com': 'Hemavathi S',
    'hsagar@lenovo.com': 'Harsh A Sagar',
    'hsikkandar@lenovo.com': 'Hassan Ul Haq Sikkandar',
    'htharkar@lenovo.com': 'Harshita Tharkar',
    'htosawad@lenovo.com': 'Harsh Tosawad',
    'hwani@lenovo.com': 'Hafid Issar Wani',
    'iahmed5@lenovo.com': 'Imran Ahmed',
    'ikhan10@lenovo.com': 'Imad Ulla Khan',
    'ikhan13@lenovo.com': 'Imdad Ulla Khan',
    'imohammed2@lenovo.com': 'M Mohammed Ibrahim',
    'inaaz@lenovo.com': 'Illahin Naaz',
    'ipujar@lenovo.com': 'Ishwar Raghu Pujar',
    'ishridhala@lenovo.com': 'Shridala Issac',
    'itasmiya@lenovo.com': 'Tasmiya Ilyas',
    'ja1@lenovo.com': 'Jagatheesh A',
    'jahmed1@lenovo.com': 'Javeed Ahmed',
    'jaltaf@lenovo.com': 'J Mohammed ALTAF',
    'jarthi@lenovo.com': 'J Arthi',
    'jbehera@lenovo.com': 'Janmejaya Behera',
    'jchinnamuthu@lenovo.com': 'Jayasankar Chinnamuthu',
    'jchoudhury1@lenovo.com': 'Jaber Choudhury',
    'jd5@lenovo.com': 'Javeed S D',
    'jdutta@lenovo.com': 'Jayashree Dutta',
    'ji@lenovo.com': 'I Javeed Shareef',
    'jjohn5@lenovo.com': 'Jithin V John',
    'jjose2@lenovo.com': 'Jibin Jose',
    'jkalita@lenovo.com': 'Jahnabi Kalita',
    'jm13@lenovo.com': 'Jeevan M',
    'jm7@lenovo.com': 'Jagannath M',
    'jn5@lenovo.com': 'Jeeva Dharshan N',
    'jp4@lenovo.com': 'Jyothsna P',
    'jr4@lenovo.com': 'Jayaram R Malagi',
    'jraj3@lenovo.com': 'Jashwanth Raj J R',
    'js10@lenovo.com': 'Jaikumar S',
    'js18@lenovo.com': 'JALAJAKSHI S',
    'js8@lenovo.com': 'Junaid Ahmed S',
    'jsingh27@lenovo.com': 'Jyoti Singh',
    'kacharya@lenovo.com': 'Kalpana Acharya',
    'kbhakta@lenovo.com': 'Kedarnath Bhakta',
    'kbhattacharj@lenovo.com': 'KAMONASISH BHATTACHARJEE',
    'kcd@lenovo.com': 'Kishore C D',
    'khebballi@lenovo.com': 'Karan  R Hebballi',
    'khusen@lenovo.com': 'Kizar Husen M',
    'kjs@lenovo.com': 'Kiran Kumar J B',
    'kkamat@lenovo.com': 'Kartik Gajanan Kamat',
    'kkanishka@lenovo.com': 'Kanishka',
    'kkomal@lenovo.com': 'Komal',
    'kln@lenovo.com': 'Kiran Kumar Ln',
    'km9@lenovo.com': 'Kubendra P M',
    'kmanjunath@lenovo.com': 'Manjunath Sahadev Kumbar',
    'kmayanglamba@lenovo.com': 'Kisher kumar Mayanglambam',
    'kpodey@lenovo.com': 'Kiran Balkrushna Podey',
    'kpratibha@lenovo.com': 'Pratibha Yeshwant Kamble',
    'kr10@lenovo.com': 'KOMATHI R',
    'kr5@lenovo.com': 'Kantharaj R',
    'kramadass@lenovo.com': 'Karthi Ramadass',
    'kravindra1@lenovo.com': 'Kanire Harshvardhan Ravindra',
    'krevanth@lenovo.com': 'Kommineni Revanth',
    'ks26@lenovo.com': 'Kesavan S',
    'ks3@lenovo.com': 'Kiran S',
    'kshaista@lenovo.com': 'Shaista Khanam',
    'kshashi@lenovo.com': 'Shashikumar D Y',
    'kshree@lenovo.com': 'Kavyashree',
    'kshubham@lenovo.com': 'Shubham Navanath Kolape',
    'ksmita@lenovo.com': 'Smita Kumari',
    'kvishal1@lenovo.com': 'Vishal Kumar',
    'lacharjee@lenovo.com': 'Lady Diana Acharjee',
    'lbhambri@lenovo.com': 'Litesh Bhambri',
    'lediga@lenovo.com': 'Ediga Likhitha',
    'lkhan@lenovo.com': 'Liyakathali Mohameth Khan',
    'lkonidhala@lenovo.com': 'Konidhala Laalasa',
    'lmawia@lenovo.com': 'Lalro Mawia',
    'ln3@lenovo.com': 'Lokesh N',
    'lreddy2@lenovo.com': 'Lavanya  Reddy C',
    'ls5@lenovo.com': 'Likith S',
    'lsharma1@lenovo.com': 'Lalan Kumar Sharma',
    'lsingha@lenovo.com': 'Luwangsana Singha',
    'ma10@lenovo.com': 'A Mohammed Yunus',
    'mafroz@lenovo.com': 'M Afroz',
    'mahmed4@lenovo.com': 'Mohd Hameed Ahmed',
    'mandagi@lenovo.com': 'Mehraj M Andagi',
    'manne@lenovo.com': 'A Manjunatha',
    'manniyappan@lenovo.com': 'Manikandan Anniyappan',
    'mansari5@lenovo.com': 'Md Akram Ansari',
    'masad@lenovo.com': 'Muhammad Asad',
    'masangi@lenovo.com': 'Manjunath Suresh Asangi',
    'mb11@lenovo.com': 'Mohammed Sahil Khan B',
    'mb6@lenovo.com': 'Mohammed Fareed B',
    'mbanu1@lenovo.com': 'Mehanaaz Banu',
    'mbasumatary@lenovo.com': 'Mitali Basumatary',
    'mbeura@lenovo.com': 'Madhusmita Beura',
    'mbommana@lenovo.com': 'Mythri Sri Bommana',
    'mbose1@lenovo.com': 'Mounabrata Bose',
    'mdhoolappana@lenovo.com': 'Manjula R Dhoolappanavar',
    'mdubule@lenovo.com': 'Mayur Mahadev Dubule',
    'mfouzan@lenovo.com': 'Mohammed Ismail Alias Fouzan',
    'mfraaz@lenovo.com': 'Mohammed Fraaz',
    'mg6@lenovo.com': 'MD Gulam G',
    'mgarg1@lenovo.com': 'Milan Garg',
    'mgowda2@lenovo.com': 'Mokshith K  Gowda',
    'mhalik@lenovo.com': 'Mohamed Halik A',
    'mhussain3@lenovo.com': 'Mudabir Hussain',
    'mhussain4@lenovo.com': 'Mohammad Arman Hussain',
    'mhussain9@lenovo.com': 'Mohammed  Hussain',
    'mingin@lenovo.com': 'Manjunath',
    'miqbal@lenovo.com': 'MD SHAMSHAD IQBAL',
    'mjabbar@lenovo.com': 'MARWAN FAHAD FAIZ JABBAR',
    'mjayasheelan@lenovo.com': 'Madhusudhan Jayasheelan',
    'mjoseph3@lenovo.com': 'Mervin Joseph',
    'mjunaid2@lenovo.com': 'J Mohammad Junaid',
    'mkaif@lenovo.com': 'Mohd  Kaif',
    'mkaleem1@lenovo.com': 'Mohamed Kaleem',
    'mkamil@lenovo.com': 'Muhammed Kamil',
    'mkazi@lenovo.com': 'Muhammadbahlool A Kazi',
    'mkeshri@lenovo.com': 'Meghna Keshri',
    'mkhaja1@lenovo.com': 'M Mohammed Khaja',
    'mkhaja@lenovo.com': 'Mohammad Khaja',
    'mkhan15@lenovo.com': 'Md Aurangjeb Khan',
    'mkhan16@lenovo.com': 'Mohammad Mansoor Khan',
    'mkhan23@lenovo.com': 'MUBASSIR KHAN',
    'mkhan27@lenovo.com': 'Mohammed Asif Khan',
    'mkhan42@lenovo.com': 'Patan Musharraf Khan',
    'mkr@lenovo.com': 'Manikanta Kr',
    'mkumar18@lenovo.com': 'Manas Kumar',
    'mkumar26@lenovo.com': 'Mrinmoy Ganguly Kumar',
    'mkumari2@lenovo.com': 'KUMARI MANJUSRI DEVI',
    'mm10@lenovo.com': 'Meghana T M',
    'mm28@lenovo.com': 'Manjunath .',
    'mm47@lenovo.com': 'Mohammed  Faraz M',
    'mm48@lenovo.com': 'Mithun M',
    'mmaanish@lenovo.com': 'Mohammed Maanish',
    'mmadni@lenovo.com': 'Mohammed Taha Madni',
    'mmahadev1@lenovo.com': 'Mahadev .',
    'mmallikarjun@lenovo.com': 'MALLIKARJUNA',
    'mmandloi@lenovo.com': 'Manish Mandloi',
    'mmanjushree@lenovo.com': 'Manjushree R',
    'mmansoor@lenovo.com': 'Mohammad Mansoor',
    'mmultani@lenovo.com': 'Muskan Meerasab Multani',
    'mmustaqeem1@lenovo.com': 'Mohammed Mustaqeem',
    'mp6@lenovo.com': 'MOHAMMEDIDRIS P',
    'mpathi@lenovo.com': 'Manas Ranjan Pathi',
    'mpatil6@lenovo.com': 'Malhari  Manohar Patil',
    'mr13@lenovo.com': 'Manoj Kumar R',
    'mrazzaq@lenovo.com': 'Mohammed Abdul Razzaq',
    'mroushan1@lenovo.com': 'Mohammed Roushan A Z',
    'ms19@lenovo.com': 'Moulana Shariff S',
    'msaddiq@lenovo.com': 'Mohammed Jafar Saddiq Jamkhandi B',
    'msaha3@lenovo.com': 'Mouli Saha',
    'msaif1@lenovo.com': 'Mohammed  Saif M A',
    'msajid@lenovo.com': 'Mohammad Sajid',
    'msamantaray@lenovo.com': 'Mohit Samantaray',
    'msaqib@lenovo.com': 'Mohammed Saqib',
    'msaquib2@lenovo.com': 'C Mohammed Saquib',
    'msaud1@lenovo.com': 'Mohammed Saud Ur Rahman',
    'msaxena@lenovo.com': 'Manish Saxena',
    'msayeed@lenovo.com': 'MUZAMMIL SAYEED',
    'mshadab1@lenovo.com': 'Mudassir Shadab',
    'mshaik5@lenovo.com': 'Shaik Mohammed Maaz',
    'mshariq1@lenovo.com': 'V Mohammed Shariq',
    'msheikh@lenovo.com': 'Muhammed Ameen Sheikh',
    'mshukla@lenovo.com': 'Madhukar Shukla',
    'msingh26@lenovo.com': 'Megha Singh',
    'msingh28@lenovo.com': 'Madhusudan Singh',
    'msingha@lenovo.com': 'Mousumi Singha',
    'msmit@lenovo.com': 'Miyani Smit Karamshibhai',
    'mt4@lenovo.com': 'Martin T',
    'mtaj@lenovo.com': 'Mubeen Taj J M',
    'mtamang@lenovo.com': 'Mishal  Tamang',
    'mtanveer@lenovo.com': 'Shaik Mohammad Tanveer',
    'mulla1@lenovo.com': 'Mohamed Haseeb Ulla',
    'muvaze@lenovo.com': 'C. Mohammed Uvaze',
    'my1@lenovo.com': 'Megha Y',
    'my2@lenovo.com': 'Mohammed Sultan R Y',
    'mzubair1@lenovo.com': 'Mohammed Zubair',
    'mzubair2@lenovo.com': 'Mohammed Zubair',
    'na4@lenovo.com': 'Navyashri  P A',
    'nahmed3@lenovo.com': 'Nayeem Ahmed',
    'nb3@lenovo.com': 'Nethravathi B',
    'nbabu@lenovo.com': 'Nagendra Babu',
    'nbegum@lenovo.com': 'NAGMA BEGUM',
    'nbhattacharj@lenovo.com': 'Neha Bhattacharjee',
    'nchithe@lenovo.com': 'Umme Kulsum Nikhat Chithe',
    'ndas3@lenovo.com': 'Noopur Das',
    'nediga@lenovo.com': 'EDIGA NAGAMANI',
    'ngadagwale@lenovo.com': 'Nikita Gadagwale',
    'nganachari@lenovo.com': 'Nivedita S  Ganachari',
    'ngunde@lenovo.com': 'Namrata Gunde',
    'njain18@lenovo.com': 'Navyaa Jain',
    'nkamate@lenovo.com': 'Nivedita Kamate',
    'nkhanum1@lenovo.com': 'Nafiya Khanum',
    'nkumar11@lenovo.com': 'Nitya Varun Kumar',
    'nkumar46@lenovo.com': 'Nikhil Kumar',
    'nkumari7@lenovo.com': 'Nikitha A',
    'nkumari@lenovo.com': 'Neha Kumari',
    'nm5@lenovo.com': 'Nikhil K M',
    'nm6@lenovo.com': 'Nambirajan',
    'nmalode@lenovo.com': 'Neha Rajkumar Malode',
    'nmunshi@lenovo.com': 'Needa K Munshi',
    'nn4@lenovo.com': 'Nikhil N',
    'nnagaraj3@lenovo.com': 'Nithish Kumar N',
    'nnaik2@lenovo.com': 'Naveen Shivram Naik',
    'nnarayanasw1@lenovo.com': 'Nalina Narayanaswamy',
    'nnayak@lenovo.com': 'Nimanshu Kumar Nayak',
    'npatil3@lenovo.com': 'Namrata Madan Patil',
    'npatiyal@lenovo.com': 'Niharika Patiyal',
    'nr2@lenovo.com': 'Nethravathi R',
    'nr3@lenovo.com': 'Naveen R',
    'nr4@lenovo.com': 'Nagaraj R',
    'nra@lenovo.com': 'Najiha Nihal R A',
    'ns8@lenovo.com': 'Nikhil S',
    'nshahid@lenovo.com': 'Shahid Nabi Shah',
    'nsharma25@lenovo.com': 'Narottam Kumar Sharma',
    'nsirsi1@lenovo.com': 'Naveed Z Ahmad Sirsi',
    'nsonar@lenovo.com': 'Nehal P Sonar',
    'ntaj@lenovo.com': 'Nazmeen Taj',
    'nts1@lenovo.com': 'Narasim Raj T S',
    'nvaishnav@lenovo.com': 'Neha Vaishnav',
    'obiswakarma@lenovo.com': 'Om Prakash Biswakarma',
    'omalavi@lenovo.com': 'Omkar K Malavi',
    'orane@lenovo.com': 'Omkar Malhar Rane',
    'oshinde@lenovo.com': 'Omkar',
    'pahmed1@lenovo.com': 'Parveez Ahmed',
    'pambli@lenovo.com': 'Prakash Ambli',
    'panusha@lenovo.com': 'Anusha P',
    'pbaliarsingh@lenovo.com': 'Pallishree Baliarsingh',
    'pbarik1@lenovo.com': 'Preeti Pragyan Barik',
    'pbn@lenovo.com': 'Prakruthi B N',
    'pcs1@lenovo.com': 'Pavithra C S',
    'pcutinha@lenovo.com': 'Praveen Nelson Cutinha',
    'pdeka2@lenovo.com': 'Pranabjyoti Deka',
    'pdubey@lenovo.com': 'Priyanshu Dubey',
    'pghosh2@lenovo.com': 'PARAMITA GHOSH',
    'pgiri@lenovo.com': 'Pramod Kumar Giri',
    'pgoswami1@lenovo.com': 'Prasenjit Goswami',
    'phanje@lenovo.com': 'Priyanka Pradyumnakumar Hanje',
    'pj@lenovo.com': 'PRAMODH J',
    'pjadhav1@lenovo.com': 'Punithraj Sakaram Jadhav',
    'pjena@lenovo.com': 'Punyatoya Jena',
    'pkittur@lenovo.com': 'Pratik Tejkumar Kittur',
    'pkulkarni2@lenovo.com': 'Pavan Kulkarni',
    'pkulkarni5@lenovo.com': 'Pavan P Kulkarni',
    'pkulkarni6@lenovo.com': 'Pushpa R Kulkarni',
    'pkulkarni7@lenovo.com': 'Prajwal Kulkarni',
    'pkumar33@lenovo.com': 'Praveen Kumar M',
    'pkumar82@lenovo.com': 'Prashant Kumar',
    'pkumar90@lenovo.com': 'Pritam Kumar',
    'pkumari13@lenovo.com': 'Priya Kumari',
    'pl2@lenovo.com': 'Prashanth L',
    'pmalviya1@lenovo.com': 'Prakash Malviya',
    'pmandal@lenovo.com': 'Prem Kumar Mandal',
    'pmandre@lenovo.com': 'Pratham V Mandre',
    'pmaruche@lenovo.com': 'PANDURANG MARUCHE',
    'pmohapatra@lenovo.com': 'Priyambada mohapatra',
    'pmutagekar@lenovo.com': 'Prem Prashant Mutagekar',
    'pn2@lenovo.com': 'N Pranay',
    'pnaidu2@lenovo.com': 'Prarena B Naidu',
    'pnayak3@lenovo.com': 'Pratisruti Nayak',
    'pojha@lenovo.com': 'Prayash Kumar Ojha',
    'pp14@lenovo.com': 'Priya P',
    'ppagey@lenovo.com': 'Pooja Pagey',
    'ppaudel1@lenovo.com': 'POOJA PAUDEL',
    'ppk2@lenovo.com': 'Pruthviraj P K',
    'ppriya4@lenovo.com': 'Pragati  Priya',
    'ppriyadarsi1@lenovo.com': 'Payal Priyadarsini',
    'pr20@lenovo.com': 'Punith B R',
    'prajak@lenovo.com': 'Pradyumna Rajak',
    'prajanna@lenovo.com': 'Poornima R',
    'prathod1@lenovo.com': 'Prakash Rathod',
    'preddy4@lenovo.com': 'S Praveen Kumar Reddy',
    'prout@lenovo.com': 'Prachi Pragnya Rout',
    'proy1@lenovo.com': 'Purnendu Shekhar Roy',
    'ps5@lenovo.com': 'Pavan S',
    'psaikia@lenovo.com': 'Paridhi Prisha Saikia',
    'psaw1@lenovo.com': 'PITAMBER SAW',
    'psen@lenovo.com': 'Pragya Sen',
    'pshetty2@lenovo.com': 'PUSHPRAJ NARAYAN SHETTY',
    'pshirgave@lenovo.com': 'Pooja Shirgave',
    'psingh44@lenovo.com': 'Priyanshu Kumar Singh',
    'psivanandam@lenovo.com': 'Prasannaa Sivanandam',
    'pswain@lenovo.com': 'Pratikshaya priyadarsini swain',
    'ptippanna@lenovo.com': 'Puranik Tippanna',
    'ra11@lenovo.com': 'Ruksana A',
    'ra13@lenovo.com': 'Rakshitha A',
    'rahmed3@lenovo.com': 'Riyazahmad Mahmadrafiq Ramadurg',
    'rap@lenovo.com': 'Rajesh A P',
    'rarif1@lenovo.com': 'Md Rizwan Arif',
    'rbhanumurthy@lenovo.com': 'Rahul Bhanumurthy',
    'rbr@lenovo.com': 'Roopa Shree  Br',
    'rcc_north@lenovo.com': 'Neetu Kumar',
    'rd3@lenovo.com': 'RUTH D',
    'rdevi@lenovo.com': 'Rashmi Devi',
    'rfernandez4@lenovo.com': 'Romeo Fernandez',
    'rgovind1@lenovo.com': 'Ram Govinda Lattya',
    'rgupta22@lenovo.com': 'Rishav Gupta',
    'rjolad@lenovo.com': 'Rohit Jolad',
    'rk3@lenovo.com': 'Rinu P K',
    'rkaif@lenovo.com': 'Ruman Kaif',
    'rkiran2@lenovo.com': 'Ravi Kiran',
    'rkumar45@lenovo.com': 'Rahul Kumar',
    'rkumar72@lenovo.com': 'Rohit Kumar',
    'rkumar73@lenovo.com': 'Ravinder Kumar',
    'rkumar79@lenovo.com': 'Roshan Kumar G',
    'rkumar81@lenovo.com': 'Sushil Kumar  Rout',
    'rkumar83@lenovo.com': 'Rakesh Kumar',
    'rl@lenovo.com': 'Raju L',
    'rlakhani1@lenovo.com': 'Rehan R Lakhani',
    'rlamani@lenovo.com': 'Rajesh Lamani',
    'rloitongbam@lenovo.com': 'Robert Loitongbam',
    'rmallshetty@lenovo.com': 'Ratnashree P Mallshetty',
    'rmg@lenovo.com': 'Ramesh M G',
    'rmishra12@lenovo.com': 'Rimi',
    'rml@lenovo.com': 'Rahul M L',
    'rmondal4@lenovo.com': 'RAMKRISHNADAS MONDAL',
    'rmuddebihal@lenovo.com': 'Ruman Muddebihal',
    'rnayan@lenovo.com': 'Ritesh Nayan',
    'rojha@lenovo.com': 'Riya Ojha',
    'rp1@lenovo.com': 'Rakesh P',
    'rpandey10@lenovo.com': 'Rishikesh Pandey',
    'rpandit1@lenovo.com': 'Ram Milan Pandit',
    'rpanwar@lenovo.com': 'Richa Panwar',
    'rpasha@lenovo.com': 'Riyaz Pasha',
    'rpowar@lenovo.com': 'RUSHIKESH POWAR',
    'rprajapati@lenovo.com': 'Rajmohan Prajapati',
    'rpralhad@lenovo.com': 'Ram Pralhad',
    'rpramod@lenovo.com': 'Raghavendra Pramod Mahale',
    'rprasad11@lenovo.com': 'Rahul Prasad',
    'rr13@lenovo.com': 'Rajesh Kumar R',
    'rr16@lenovo.com': 'Ranjith R',
    'rr21@lenovo.com': 'RAKESH R',
    'rraj3@lenovo.com': 'Rishav Raj',
    'rram@lenovo.com': 'Rajendra Kumar Ram',
    'rranjan3@lenovo.com': 'Ritesh Ranjan',
    'rrevankar@lenovo.com': 'Roshan Rajendra Revankar',
    'rriyazuddin@lenovo.com': 'RIYAZUDDIN',
    'rs12@lenovo.com': 'Revathi S',
    'rs25@lenovo.com': 'Rashin S',
    'rsawant2@lenovo.com': 'Ritesh Dattaram Sawant',
    'rshaik4@lenovo.com': 'Shaik Rabbani',
    'rshetty5@lenovo.com': 'Rohith N Shetty',
    'rshukla5@lenovo.com': 'Rajneesh Kumar Shukla',
    'rsingh30@lenovo.com': 'Ram Mohan Singh',
    'rsingh51@lenovo.com': 'Rohan  Kumar Singh',
    'rsingh54@lenovo.com': 'Rohan Singh',
    'rsingh67@lenovo.com': 'Riya  Singh',
    'rsingh68@lenovo.com': 'Rahul Singh',
    'rsivakumar2@lenovo.com': 'Renju  Sivakumar',
    'rthota@lenovo.com': 'Thota Rupesh Kumar',
    'rzameer@lenovo.com': 'Roshan Zameer M A',
    'sa33@lenovo.com': 'Soni A',
    'sab@lenovo.com': 'Suhas Ab',
    'sadil@lenovo.com': 'Shaik  Mohamad Adil',
    'safreedi1@lenovo.com': 'Shaikh Mohammed Afreedi',
    'sahmed17@lenovo.com': 'Shaik Sameer Ahmed',
    'sahmed18@lenovo.com': 'Shaik Kota Ejaz Ahmed',
    'sahmed20@lenovo.com': 'Shaik Muddassir Ahmed',
    'sakbar1@lenovo.com': 'Syed Akbar Shariff',
    'sakram@lenovo.com': 'Syed Waseem Akram',
    'salam3@lenovo.com': 'Md Shabbir Alam',
    'sali4@lenovo.com': 'Shahzad Ali',
    'sali7@lenovo.com': 'Syed Shahabaz Ali',
    'salthaf@lenovo.com': 'Shaik  Althaf',
    'sanjum3@lenovo.com': 'SHAIK ANISA ANJUM',
    'sarbaz@lenovo.com': 'Syed Arbaz',
    'sarshiya@lenovo.com': 'Shaik Ruhina Arshiya',
    'sashvitha@lenovo.com': 'S Ashvitha',
    'sawasthi2@lenovo.com': 'SAVINAY AWASTHI',
    'sbaba1@lenovo.com': 'Sayed Suhail Baba',
    'sbandodkar@lenovo.com': 'Siddhant Gulab Bandodkar',
    'sbanerjee13@lenovo.com': 'Saptarshi Banerjee',
    'sbanu3@lenovo.com': 'Sayera Banu',
    'sbasha7@lenovo.com': 'Shaik Basha',
    'sbehera3@lenovo.com': 'Surya Narayan Behera',
    'sbehera8@lenovo.com': 'Swati Behera',
    'sbharti1@lenovo.com': 'Sakshi Bharti',
    'sbhattachar2@lenovo.com': 'Sohini Bhattacharya',
    'sbhosale@lenovo.com': 'Snehal S Bhosale',
    'sbhui@lenovo.com': 'Suman Bhui',
    'sbidari@lenovo.com': 'Siddharth Shivakumar Bidari',
    'sbiradar2@lenovo.com': 'SAHANA B BIRADAR',
    'sbiredar@lenovo.com': 'Santosh Kumar Biredar',
    'sbiswal1@lenovo.com': 'Subham Kumar Biswal',
    'sc7@lenovo.com': 'Santosh B C',
    'schavan4@lenovo.com': 'Saneel S Chavan',
    'schoudhury4@lenovo.com': 'Shahriar H Choudhury',
    'scm1@lenovo.com': 'Sowmya C M',
    'sd15@lenovo.com': 'Sujith kumar',
    'sd7@lenovo.com': 'Surjith Singh B D',
    'sd@lenovo.com': 'Solomon D',
    'sdas30@lenovo.com': 'Shreya Das',
    'sdas7@lenovo.com': 'Sandeep Das',
    'sdeshpande2@lenovo.com': 'Shruthi P Deshpande',
    'sdevi1@lenovo.com': 'Surabhi Devi',
    'sdey1@lenovo.com': 'Sumith Kumar Dey',
    'sdey5@lenovo.com': 'Subhadip Dey',
    'sdhal@lenovo.com': 'Sruti Priyadarsini Dhal',
    'sdiwan@lenovo.com': 'Shiva Anand Diwan',
    'sdutta4@lenovo.com': 'Sougata Dutta',
    'sdwivedi@lenovo.com': 'Saurabh Dwivedi',
    'sfarhan@lenovo.com': 'Syed  Mohammed Farhan',
    'sfathima3@lenovo.com': 'Rachanvale Saba Fathima',
    'sfazal@lenovo.com': 'Syed Fazal',
    'sgadad@lenovo.com': 'Shrushti Gadad',
    'sgaur@lenovo.com': 'Subendra Gaur',
    'sghousia@lenovo.com': 'Sha Ghousia M',
    'sgope@lenovo.com': 'Sawan Kumar Gope',
    'sgoswami1@lenovo.com': 'Sweta Goswami',
    'sgoyal1@lenovo.com': 'Suhani',
    'sh4@lenovo.com': 'Shoaib Ur Rahman H',
    'shallad@lenovo.com': 'Somshekar Banappa Hallad',
    'shanish@lenovo.com': 'Singitham Hanish',
    'shapis@motorola.com': 'SHAPI',
    'sharbab@lenovo.com': 'Sandip Harbab',
    'shikmathulla@lenovo.com': 'Syed Hikmathullah',
    'shs@lenovo.com': 'Syed Sadath HS',
    'shussain4@lenovo.com': 'Shameer Hussain',
    'si2@lenovo.com': 'Syed Mohammed Umer S I',
    'simran5@lenovo.com': 'Shaik Imran',
    'sirshad@lenovo.com': 'Shaik Mohammad Irshad',
    'sjana1@lenovo.com': 'Subrata Jana',
    'sjawalge@lenovo.com': 'Shubhangi Jawalge',
    'sjena3@lenovo.com': 'Smarakee Jena',
    'sjn@lenovo.com': 'Subhan J N',
    'sk20@lenovo.com': 'Sarafudeen K',
    'skadam1@lenovo.com': 'Shivaji Kadam',
    'skage@lenovo.com': 'Sushma Mahaveer Kage',
    'skarmakar1@lenovo.com': 'Sibam Karmakar',
    'skarthik@lenovo.com': 'Natakam Somesh Karthik',
    'skeshwapur@lenovo.com': 'Sanjota Y Keshwapur',
    'skhan33@lenovo.com': 'Samiullah Khan I',
    'skhan37@lenovo.com': 'Shanawaz Khan',
    'skhan42@lenovo.com': 'Shueib Khan',
    'skhan43@lenovo.com': 'Shafayath  Ulla Khan',
    'skibriya@lenovo.com': 'Shaik Kibriya',
    'skolkar@lenovo.com': 'Snehal S Kolkar',
    'skousar@lenovo.com': 'Saniya Kousar',
    'skulkarni11@lenovo.com': 'Sourabha K Kulkarni',
    'skumar130@lenovo.com': 'Sachin  Kumar',
    'skumar18@lenovo.com': 'Sathish Kumar V',
    'skumar77@lenovo.com': 'Sharvan Kumar',
    'skumar82@lenovo.com': 'Kumar Saurabh',
    'skumari20@lenovo.com': 'Shweta Kumari',
    'skumari9@lenovo.com': 'Sindhu Kumari',
    'slal@lenovo.com': 'Seema Lal',
    'sluqmaan@lenovo.com': 'Syed Luqmaan',
    'sm21@lenovo.com': 'Subhani M',
    'sm28@lenovo.com': 'Sarvesh M',
    'sm45@lenovo.com': 'SIDDALINGIAH SWAMY H M',
    'sm56@lenovo.com': 'Suhas B M',
    'sm69@lenovo.com': 'Shwetha  M',
    'smahanty@lenovo.com': 'Swarnika Mahanty',
    'smaheen@lenovo.com': 'Syed Maheen',
    'smalli@lenovo.com': 'Sneha Malli',
    'smanga@lenovo.com': 'Sania Mangar',
    'smanna@lenovo.com': 'Sushanta Manna',
    'smenon4@lenovo.com': 'Sreejith Menon',
    'smenon6@lenovo.com': 'S. Sudhir Menon',
    'smishra22@lenovo.com': 'Subhranshu Mishra',
    'smn@lenovo.com': 'M N Shruthi',
    'smohammedi@lenovo.com': 'Shifa Mohammedi',
    'smollick@lenovo.com': 'Saifuddin Mollick',
    'smubarak@lenovo.com': 'Shaik Mubarak',
    'smuduli1@lenovo.com': 'Subrat Muduli',
    'smulla@lenovo.com': 'Salman Rafiq Mulla',
    'smundepi@lenovo.com': 'Saurabh Mundepi',
    'sn6@lenovo.com': 'Sushma N',
    'snagpure@lenovo.com': 'SHREYASH VIJAY NAGPURE',
    'snamala@lenovo.com': 'Namala Sirisha',
    'snaskar@lenovo.com': 'Samya Naskar',
    'snasreen@lenovo.com': 'Shaik Nasreen',
    'snayak7@lenovo.com': 'Shruti Nayak',
    'snigam1@lenovo.com': 'Sachin Kumar Nigam',
    'snishath@lenovo.com': 'Saniya Nishath',
    'snv@lenovo.com': 'Sunil N V',
    'spal4@lenovo.com': 'Supriya  .',
    'spanda2@lenovo.com': 'Suresh Panda',
    'spanda6@lenovo.com': 'Sasmita Panda',
    'spanda7@lenovo.com': 'Swayam Sampanna Panda',
    'sparmar@lenovo.com': 'Sahil Parmar',
    'spasha4@lenovo.com': 'Saleem  Pasha E',
    'spatil13@lenovo.com': 'Sneha V Patil',
    'spatil16@lenovo.com': 'Swapnil Sanjay Patil',
    'spatil5@lenovo.com': 'Shubhangi Suresh Patil',
    'spattanaik@lenovo.com': 'SOUMYA RANJAN PATTANAIK',
    'spawar6@lenovo.com': 'Sakshi Prashant Pawar',
    'spetkar@lenovo.com': 'Samarth Petkar',
    'spinto@lenovo.com': 'Steven Mario  Pinto',
    'spoojary@lenovo.com': 'Sandesh',
    'sprasad8@lenovo.com': 'Subham Prasad',
    'spriya3@lenovo.com': 'S Lakshmi Priya',
    'spriyadarsh2@lenovo.com': 'Sudhanshu Ranjan  Priyadarshi',
    'spriyadarshi@lenovo.com': 'SMITIKA PRIYADARSHINI ROUT',
    'sr18@lenovo.com': 'Suresh R',
    'sr33@lenovo.com': 'SUDARSHAN R',
    'srai4@lenovo.com': 'Shekhar Rai',
    'sraj11@lenovo.com': 'Sudhir Raj',
    'srajendra@lenovo.com': 'Swami Ratnamala Rajendra',
    'srajkumar@lenovo.com': 'SOUMYA RAJKUMAR',
    'sram1@lenovo.com': 'Sonu Kumar Ram',
    'srao4@lenovo.com': 'Sharath Nagaraj Rao',
    'srasool@lenovo.com': 'Shaik Mahammad Rasool',
    'sray2@lenovo.com': 'Surbhi Ray',
    'sray4@lenovo.com': 'Sandip Kumar Ray',
    'sreddy6@lenovo.com': 'Shaparpod Santhosh Reddy',
    'sroshini@lenovo.com': 'S Roshini',
    'ss104@lenovo.com': 'Shafee Vullah S',
    'ss24@lenovo.com': 'Sunil S',
    'ss29@lenovo.com': 'Sunil Kumar S',
    'ss38@lenovo.com': 'Shrikant S',
    'ss41@lenovo.com': 'Swathish S',
    'ss43@lenovo.com': 'Satish Kumar S',
    'ss53@lenovo.com': 'S Sharan',
    'ss68@lenovo.com': 'Shreyas S',
    'ssahoo9@lenovo.com': 'Suryakant Sahoo',
    'ssahu5@lenovo.com': 'Soumya Subhadarsini Sahu',
    'ssaifulla@lenovo.com': 'Syed Saifulla',
    'ssameer@lenovo.com': 'Shafiulla Sameer',
    'ssaniya@lenovo.com': 'S B Saniya',
    'ssaurav@lenovo.com': 'SHUBHAM SAURAV',
    'sshafi2@lenovo.com': 'Syed Mahammed Shafi',
    'sshalini@lenovo.com': 'Shubra Shalini',
    'ssharma33@lenovo.com': 'Shivsagar V Sharma',
    'sshinde3@lenovo.com': 'Sachin Suresh Shinde',
    'sshinde5@lenovo.com': 'SHRIKANT H SHINDE',
    'sshirshi@lenovo.com': 'Shiva Kumar',
    'sshree1@lenovo.com': 'Sushma Shree',
    'sshruti1@lenovo.com': 'Shruti .',
    'sshukla4@lenovo.com': 'Sudhanshu Shukla',
    'ssingh42@lenovo.com': 'SARVESH KUMAR SINGH',
    'ssingh64@lenovo.com': 'Suraj Singh',
    'ssingh82@lenovo.com': 'Sejal Singh',
    'ssinha11@lenovo.com': 'Shambhavi Sinha',
    'ssinha6@lenovo.com': 'SUNIT SINHA',
    'ssneha1@lenovo.com': 'Sneha S',
    'ssrinivas2@lenovo.com': 'Satya Srinivas Pichika',
    'ssubhi@lenovo.com': 'Shubhangi Subhi',
    'ssudharani@lenovo.com': 'Sudharani .',
    'ssuhel@lenovo.com': 'Shaik Reddy Suhel',
    'ssurkod@lenovo.com': 'Subhashgouda Surkod',
    'ssushmashri@lenovo.com': 'Sushmashri',
    'st13@lenovo.com': 'Snehan Thejaswi T',
    'stalukder1@lenovo.com': 'Sutabh Talukder',
    'stanzeem@lenovo.com': 'Sheik Tanzeem',
    'sthakur10@lenovo.com': 'Saloni Thakur',
    'sthouseef@lenovo.com': 'Shaik Mohammad Thouseef',
    'stippanna@lenovo.com': 'Saraswati Tippanna Bharamannavar',
    'supadhyay1@lenovo.com': 'Sagar Rajendra Upadhyay',
    'svali@lenovo.com': 'Shaik Murasha Vali',
    'svenkatesh2@lenovo.com': 'Srinidhi Venkatesh',
    'svenkatraman@lenovo.com': 'SIVA VENKATRAMAN',
    'syadav9@lenovo.com': 'Shiv Kumar Yadav',
    'syaseen@lenovo.com': 'Syed Yaseen',
    'syenagi@lenovo.com': 'SIDDHESHWAR YENAGI',
    'syinkaka@lenovo.com': 'Sandeep Kakadala',
    'tahamed2@lenovo.com': 'Thowqeer Ahamed',
    'tahmed10@lenovo.com': 'Tanzil  Ahmed',
    'takram@lenovo.com': 'Tinker Waseem Akram',
    'tfathima1@lenovo.com': 'Tahseen Fathima M',
    'tkharvi@lenovo.com': 'Tanish R Kharvi',
    'tkuppusamy@lenovo.com': 'Tirumalai Kuppusamy',
    'tl@lenovo.com': 'Tamizharasan L',
    'tn1@lenovo.com': 'Tanuja A N',
    'tn6@lenovo.com': 'Tasmiya Khanum N',
    'tpasha@lenovo.com': 'Tabrez Pasha',
    'tpatel2@lenovo.com': 'Tasleem Patel',
    'tr5@lenovo.com': 'Tharun R',
    'uatavalgi@lenovo.com': 'Ujwalkumar Atavalgi',
    'uhonnalli1@lenovo.com': 'Umarfarooq R Honnalli',
    'ukhan@lenovo.com': 'Usman Khan',
    'um2@lenovo.com': 'Udhayanithi M',
    'va10@lenovo.com': 'Varshitha A',
    'va5@lenovo.com': 'A. Vellangani',
    'vamalkumar@lenovo.com': 'Vaishnavi Amalkumar',
    'varatti@lenovo.com': 'Vinayak Aratti',
    'vb6@lenovo.com': 'VINAY B',
    'vbasidoni@lenovo.com': 'Vaishnavi Basidoni',
    'vbhovi1@lenovo.com': 'Vikas B Bhovi',
    'vbiradar@lenovo.com': 'Veeresh Biradar',
    'vchandrashe2@lenovo.com': 'V Chandra Shekhar',
    'vck@lenovo.com': 'CIRISETKONDAPPAVEERANJAN',
    'vd2@lenovo.com': 'Venkata Chalapathi S D',
    'vd6@lenovo.com': 'Vivekananda D',
    'vd@lenovo.com': 'Vicky Diengdoh',
    'vgovankop@lenovo.com': 'Vaibhavi Sadanand Govankop',
    'vhampiholli@lenovo.com': 'Vijay Hampiholli',
    'vkamthane@lenovo.com': 'Vaishnavi',
    'vkulkarni4@lenovo.com': 'Vaishnavi Vaman Kulkarni',
    'vkumar18@lenovo.com': 'Vishal Kumar',
    'vkumar38@lenovo.com': 'Vipin K',
    'vkumar42@lenovo.com': 'Vinodh Kumar',
    'vkumar52@lenovo.com': 'Vikash Kumar',
    'vkumar62@lenovo.com': 'Vikas Kumar',
    'vkumar64@lenovo.com': 'Vikas Kumar',
    'vkumar72@lenovo.com': 'Vickey Kumar',
    'vkumar82@lenovo.com': 'Vikrant Kumar',
    'vkumar88@lenovo.com': 'Vinod Kumar R',
    'vkumar9@lenovo.com': 'Vimal Kumar V',
    'vmahalakshmi@lenovo.com': 'V MAHALAKSHMI',
    'vmanjunath@lenovo.com': 'Manjunath V',
    'vmishra5@lenovo.com': 'Vivek Kumar Mishra',
    'vnavalgundma@lenovo.com': 'Vachan Navalgundmath',
    'vp5@lenovo.com': 'Vinoth P',
    'vpandey6@lenovo.com': 'Vishal Pandey',
    'vprabhu@lenovo.com': 'Vijay Prabhu V',
    'vrotti@lenovo.com': 'Vishal Rotti',
    'vsb@lenovo.com': 'Vandana SB',
    'vsharma11@lenovo.com': 'Vinay Kumar Sharma',
    'vsharma30@lenovo.com': 'Virat Sharma',
    'vsharma32@lenovo.com': 'Vimal Sharma',
    'vshivgunde@lenovo.com': 'Vidya Virpakshi Shivgunde',
    'vshukla2@lenovo.com': 'Vedansh Shukla',
    'vsinha@lenovo.com': 'Vikash Ranjan Sinha',
    'vsuresh1@lenovo.com': 'Varada Suresh',
    'vt1@lenovo.com': 'T Vignesh',
    'vthakur3@lenovo.com': 'Virali Thakur',
    'vtiwari5@lenovo.com': 'Varshikey Tiwari',
    'vvijaykumar1@lenovo.com': 'Vijaykumar',
    'wakram@lenovo.com': 'Wasim Akram',
    'wjohn1@lenovo.com': 'WILLIAM JOHN',
    'wz1@lenovo.com': 'Wachema Jakeer Hussaian',
    'ybs@lenovo.com': 'Yashavantha B S',
    'yilkal@lenovo.com': 'Yunus Ilkal',
    'ykarade1@lenovo.com': 'YOGESH KARADE',
    'ysutar@lenovo.com': 'Yuvaraj Tanaji Sutar',
    'yvarma@lenovo.com': 'YALLAMRAJU GNANESWARA  VARMA',
    'zhussain@lenovo.com': 'Zakeer Hussain',
    'zkhan2@lenovo.com': 'Zubair Khan',
    'zkhatoon@lenovo.com': 'Zubeda Khatoon',
    'zmanzoor@lenovo.com': 'Zuhaib Manzoor',
    'zmoinuddin@lenovo.com': 'Mohd Zohaib Moinuddin',
    'zowais@lenovo.com': 'Mohammed Zafar Owais',
    'zz1@lenovo.com': 'Zaiba',
}


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                         EMBEDDED HTML PAGE                              ║
# ╚══════════════════════════════════════════════════════════════════════════╝
HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lenovo One Pager - IT Helpdesk Home</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    html, body {
      height: 100%;
      font-family: 'Segoe UI', Arial, sans-serif;
      background: #13131f;
      color: #fff;
    }

    body {
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }

    /* PAGE HEADING */
    .page-heading {
      background: linear-gradient(135deg, #0a0a23 0%, #1a1a4e 50%, #2d0036 100%);
      padding: 22px 36px;
      flex-shrink: 0;
      border-bottom: 3px solid #e50000;
    }
    .page-heading h1 {
      font-size: 1.7rem;
      font-weight: 900;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #fff;
      text-shadow: 0 2px 16px rgba(229,0,0,0.4);
    }
    .page-heading p {
      margin-top: 4px;
      font-size: 0.82rem;
      color: #999;
    }

    /* ANNOUNCEMENT BANNERS */
    .banner-strip {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
      padding: 14px 36px;
      background: rgba(0,0,0,0.25);
      border-bottom: 1px solid rgba(255,255,255,0.07);
      flex-shrink: 0;
    }
    .banner-card {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 10px;
      padding: 14px 18px;
      display: flex;
      align-items: flex-start;
      gap: 13px;
      min-height: 110px;
      transition: background 0.2s, border-color 0.2s;
    }
    .banner-card:hover {
      background: rgba(229,0,0,0.1);
      border-color: rgba(229,0,0,0.4);
    }
    .banner-icon { font-size: 1.5rem; flex-shrink: 0; margin-top: 2px; }
    .banner-tag {
      font-size: 0.63rem;
      font-weight: 700;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      color: #e50000;
      margin-bottom: 4px;
    }
    .banner-text {
      font-size: 0.84rem;
      color: #ccc;
      font-weight: 500;
      line-height: 1.45;
    }

    /* MAIN WRAPPER */
    .main-wrapper {
      display: flex;
      flex: 1;
      overflow: hidden;
    }

    /* SIDEBAR */
    .sidebar {
      width: 230px;
      min-width: 230px;
      background: #0e0e1c;
      border-right: 1px solid rgba(255,255,255,0.07);
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      flex-shrink: 0;
    }
    .sidebar-label {
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: #555;
      padding: 18px 20px 8px;
    }
    .nav-item {
      display: flex;
      align-items: center;
      gap: 11px;
      padding: 13px 20px;
      cursor: pointer;
      color: #aaa;
      font-size: 0.88rem;
      font-weight: 500;
      border-left: 3px solid transparent;
      transition: background 0.15s, color 0.15s, border-color 0.15s;
      user-select: none;
    }
    .nav-item:hover { background: rgba(255,255,255,0.05); color: #fff; }
    .nav-item.active {
      background: rgba(229,0,0,0.12);
      color: #fff;
      border-left-color: #e50000;
    }
    .nav-item .nav-icon { font-size: 1rem; flex-shrink: 0; width: 20px; text-align: center; }

    /* CONTENT PANEL */
    .content-panel {
      flex: 1;
      overflow-y: auto;
      background: #13131f;
      position: relative;
    }

    .panel {
      display: none;
      padding: 32px 40px;
      animation: fadeIn 0.2s ease;
    }
    .panel.active { display: block; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateX(8px); }
      to   { opacity: 1; transform: translateX(0); }
    }

    .panel-title {
      font-size: 1.3rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 22px;
      padding-bottom: 12px;
      border-bottom: 2px solid #e50000;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    /* FILE VIEWER */
    #file-viewer {
      display: none;
      flex-direction: column;
      height: 100%;
      padding: 20px 32px;
      animation: fadeIn 0.2s ease;
    }
    #file-viewer.active { display: flex; }

    .viewer-topbar {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 16px;
      flex-shrink: 0;
    }
    .btn-back {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 7px;
      color: #ccc;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s, color 0.2s;
    }
    .btn-back:hover { background: rgba(255,255,255,0.15); color: #fff; }

    .viewer-filename {
      font-size: 0.95rem;
      font-weight: 600;
      color: #fff;
      flex: 1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .btn-newtab {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      background: #e50000;
      border: none;
      border-radius: 7px;
      color: #fff;
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
      transition: background 0.2s;
      white-space: nowrap;
    }
    .btn-newtab:hover { background: #b30000; }

    .file-type-badge {
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      flex-shrink: 0;
    }
    .badge-excel { background: #1d6f42; color: #fff; }
    .badge-word  { background: #2b579a; color: #fff; }
    .badge-pdf   { background: #c0392b; color: #fff; }
    .badge-text  { background: #555;    color: #fff; }

    #viewer-frame {
      flex: 1;
      width: 100%;
      border: none;
      border-radius: 10px;
      background: #fff;
      min-height: 0;
    }

    /* LINK GRID */
    .link-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
      gap: 12px;
    }
    .link-card {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.09);
      border-radius: 10px;
      padding: 13px 14px;
      text-decoration: none;
      color: #ccc;
      font-size: 0.85rem;
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      transition: background 0.2s, border-color 0.2s, transform 0.15s, color 0.15s;
    }
    .link-card:hover {
      background: rgba(229,0,0,0.18);
      border-color: #e50000;
      color: #fff;
      transform: translateY(-2px);
    }
    .dot {
      width: 8px; height: 8px;
      border-radius: 50%;
      background: #e50000;
      flex-shrink: 0;
    }

    /* INFO CARDS */
    .card-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }
    .info-card {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 12px;
      padding: 22px;
      display: flex;
      flex-direction: column;
    }
    .info-card h3 { font-size: 1.05rem; font-weight: 700; color: #fff; margin-bottom: 4px; }
    .info-card .domain { font-size: 0.73rem; color: #666; margin-bottom: 10px; }
    .info-card p { font-size: 0.82rem; color: #aaa; line-height: 1.6; flex: 1; margin-bottom: 16px; }
    .info-card a.btn {
      display: inline-block;
      padding: 8px 18px;
      background: #e50000;
      color: #fff;
      border-radius: 6px;
      text-decoration: none;
      font-size: 0.82rem;
      font-weight: 600;
      align-self: flex-start;
      transition: background 0.2s;
    }
    .info-card a.btn:hover { background: #b30000; }

    /* DOC PILLS */
    .doc-grid { display: flex; flex-wrap: wrap; gap: 10px; }
    .doc-pill {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 9px 14px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 22px;
      text-decoration: none;
      color: #ccc;
      font-size: 0.84rem;
      font-weight: 500;
      cursor: pointer;
      transition: background 0.2s, color 0.2s, border-color 0.2s;
    }
    .doc-pill:hover { background: #e50000; color: #fff; border-color: #e50000; }
    .pill-icon { font-size: 0.82rem; }

    /* PHONE TABLE */
    .phone-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px; }
    .phone-block h3 {
      font-size: 0.9rem; font-weight: 700; color: #e50000;
      margin-bottom: 14px; text-transform: uppercase;
      letter-spacing: 1px; text-decoration: underline;
    }
    .phone-block ul { list-style: none; }
    .phone-block ul li {
      padding: 7px 0;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      font-size: 0.86rem; color: #bbb;
      display: flex; justify-content: space-between; flex-wrap: wrap; gap: 4px;
    }
    .phone-block ul li strong { color: #fff; min-width: 160px; }

    /* SOCIAL */
    .social-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 12px; }
    .social-card {
      display: flex; align-items: center; gap: 12px;
      padding: 14px 16px;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.09);
      border-radius: 10px;
      text-decoration: none; color: #bbb;
      font-size: 0.86rem; font-weight: 500;
      transition: background 0.2s, transform 0.15s, color 0.15s;
    }
    .social-card:hover { background: rgba(229,0,0,0.15); border-color: #e50000; color: #fff; transform: translateY(-2px); }
    .social-icon {
      width: 34px; height: 34px; border-radius: 8px;
      display: flex; align-items: center; justify-content: center;
      font-size: 1rem; font-weight: 700; flex-shrink: 0; color: #fff;
    }
    .fb { background: #1877f2; }
    .ig { background: linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888); }
    .yt { background: #ff0000; }
    .tw { background: #111; }
    .li { background: #0a66c2; }

    /* MDOA */
    .mdoa-form { max-width: 700px; }
    .mdoa-field { margin-bottom: 18px; }
    .mdoa-field label {
      display: block; font-size: 0.78rem; font-weight: 700;
      color: #aaa; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 7px;
    }
    .mdoa-field label span { color: #e50000; }
    .mdoa-field label small { font-weight: 400; text-transform: none; color: #666; font-size: 0.72rem; }
    .mdoa-input {
      width: 100%; padding: 10px 14px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 8px; color: #fff; font-size: 0.9rem; outline: none;
      transition: border-color 0.2s;
    }
    .mdoa-input:focus { border-color: #e50000; }
    .mdoa-input::placeholder { color: #555; }
    input[type="date"].mdoa-input::-webkit-calendar-picker-indicator { filter: invert(0.7); cursor: pointer; }
    .mdoa-btn {
      padding: 11px 30px; background: #e50000; border: none;
      border-radius: 8px; color: #fff; font-size: 0.9rem; font-weight: 700;
      cursor: pointer; transition: background 0.2s; margin-top: 6px;
    }
    .mdoa-btn:hover { background: #b30000; }
    .mdoa-result {
      margin-top: 26px; border-radius: 12px; padding: 22px 26px;
      display: none;
    }
    .mdoa-result-label {
      font-size: 0.68rem; font-weight: 700; letter-spacing: 1.2px;
      text-transform: uppercase; color: #888; margin-bottom: 14px;
    }
    .mdoa-result-grid { display: flex; gap: 36px; flex-wrap: wrap; }
    .mdoa-result-cell small { font-size: 0.68rem; color: #777; display: block; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.5px; }
    .mdoa-result-cell strong { font-size: 1.05rem; font-weight: 700; color: #fff; }
    .mdoa-result-cell.highlight strong { font-size: 1.1rem; }
    .mdoa-error {
      background: rgba(229,0,0,0.12); border: 1px solid rgba(229,0,0,0.35);
      border-radius: 10px; padding: 14px 18px; color: #ff8080;
      font-size: 0.86rem; margin-top: 18px;
    }
    .mdoa-hint {
      background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 10px; padding: 14px 18px; margin-bottom: 22px;
      font-size: 0.81rem; color: #888; line-height: 1.6;
    }
    .mdoa-hint b { color: #ccc; }

    /* FEEDBACK */
    .feedback-box {
      background: linear-gradient(135deg, #1a1a2e, #2d0036);
      border: 1px solid rgba(229,0,0,0.3);
      border-radius: 16px;
      padding: 34px 38px;
      display: flex; align-items: center;
      justify-content: space-between; gap: 24px; flex-wrap: wrap;
    }
    .feedback-box h2 { font-size: 1.4rem; font-weight: 700; margin-bottom: 8px; }
    .feedback-box p  { color: #aaa; font-size: 0.9rem; max-width: 460px; }
    .feedback-box a {
      display: inline-block; padding: 13px 28px;
      background: #fff; color: #e50000;
      font-weight: 700; font-size: 0.92rem;
      border-radius: 8px; text-decoration: none;
      white-space: nowrap; transition: background 0.2s, color 0.2s;
    }
    .feedback-box a:hover { background: #e50000; color: #fff; }

    /* FOOTER */
    footer {
      background: #09090f;
      text-align: center;
      padding: 11px;
      color: #444;
      font-size: 0.73rem;
      border-top: 1px solid rgba(255,255,255,0.06);
      flex-shrink: 0;
    }
  </style>
</head>
<body>

<!-- ANNOUNCEMENT BANNERS -->
<div class="banner-strip">

  <div class="banner-card" style="padding:0;overflow:hidden;cursor:default;">
    <img src="https://raw.githubusercontent.com/Manoj213333/lenovo-one-pager/main/banner1.png"
         alt="AI Talent Spotlight"
         style="width:100%;height:100%;object-fit:cover;border-radius:10px;display:block;" />
  </div>

  <div class="banner-card" style="padding:0;overflow:hidden;cursor:default;">
    <img src="https://raw.githubusercontent.com/Manoj213333/lenovo-one-pager/main/banner2.png"
         alt="Banner 2"
         style="width:100%;height:100%;object-fit:cover;border-radius:10px;display:block;" />
  </div>

  <div class="banner-card" style="padding:0;overflow:hidden;cursor:default;background:#000;display:flex;align-items:center;justify-content:center;">
    <img src="https://raw.githubusercontent.com/Manoj213333/lenovo-one-pager/main/banner3.png"
         alt="Banner 3"
         style="width:100%;height:auto;object-fit:contain;border-radius:10px;display:block;" />
  </div>

</div>

<!-- MAIN: SIDEBAR + CONTENT -->
<div class="main-wrapper">

  <!-- SIDEBAR -->
  <nav class="sidebar">
    <div class="sidebar-label">Sections</div>
    <div class="nav-item active" data-target="lenovo-urls">
      <span class="nav-icon">&#128279;</span> Lenovo URLs
    </div>
    <div class="nav-item" data-target="learning">
      <span class="nav-icon">&#127891;</span> Learning &amp; Development
    </div>
    <div class="nav-item" data-target="process-docs">
      <span class="nav-icon">&#128193;</span> Process Documents
    </div>
    <div class="nav-item" data-target="contact">
      <span class="nav-icon">&#128222;</span> Contact Numbers
    </div>
    <div class="nav-item" data-target="j2w">
      <span class="nav-icon">&#9889;</span> J2W URLs
    </div>
    <div class="nav-item" data-target="community">
      <span class="nav-icon">&#127760;</span> Our Community
    </div>
    <div class="nav-item" data-target="mdoa">
      <span class="nav-icon">&#128203;</span> MDOA Criteria Check
    </div>
    <div class="nav-item" data-target="feedback">
      <span class="nav-icon">&#128172;</span> Help Us Improve
    </div>
  </nav>

  <!-- CONTENT PANEL -->
  <div class="content-panel">

    <!-- FILE VIEWER -->
    <div id="file-viewer">
      <div class="viewer-topbar">
        <button class="btn-back" onclick="closeFileViewer()">&#8592; Back</button>
        <span class="file-type-badge" id="viewer-badge"></span>
        <span class="viewer-filename" id="viewer-title"></span>
        <a class="btn-newtab" id="viewer-newtab" href="#" target="_blank">Open in new tab &#8599;</a>
      </div>
      <iframe id="viewer-frame" src="" title="File Viewer"></iframe>
    </div>

    <!-- LENOVO URLs -->
    <div class="panel active" id="lenovo-urls">
      <div class="panel-title">&#128279; Lenovo URLs</div>
      <div class="link-grid">
        <a class="link-card" href="https://buyalenovo.com/" target="_blank"><span class="dot"></span>Carry-In Locator</a>
        <a class="link-card" href="https://analytics.bsharpcorp.com/open-view/104207000008114715" target="_blank"><span class="dot"></span>PUDO Status Check</a>
        <a class="link-card" href="https://todo.bsharpcorp.com/kpi/kpi_dashboard" target="_blank"><span class="dot"></span>Check Your KPI</a>
        <a class="link-card" href="https://support.lenovo.com/in/en/parts-lookup?linktrack=footer:support_parts%20lookup" target="_blank"><span class="dot"></span>Parts Look-up</a>
        <a class="link-card" href="https://pcsupport.lenovo.com/in/en/iwslookup#" target="_blank"><span class="dot"></span>IWS Warranty Check</a>
        <a class="link-card" href="https://secure.logmeinrescue.com/" target="_blank"><span class="dot"></span>LogMeIn Rescue - Web</a>
        <a class="link-card" href="https://outlook.office.com/" target="_blank"><span class="dot"></span>Outlook Web</a>
        <a class="link-card" href="https://support.lenovo.com/" target="_blank"><span class="dot"></span>Support Site</a>
        <a class="link-card" href="https://psref.lenovo.com/" target="_blank"><span class="dot"></span>PSREF</a>
        <a class="link-card" href="https://forms.office.com/pages/responsepage.aspx?id=KAt9XPi9DEGqk03zcrFiAx8XhD7PAPpHqdVcJ7FDVOdURFJXTzZHNUdWRThVSkcwNUhJODBHMTA5Ri4u&origin=lprLink&route=shorturl" target="_blank"><span class="dot"></span>Raise Lead &#8211; Laptop &amp; Accessory</a>
        <a class="link-card" href="http://103.30.234.106:8080/ui/ad/v1/index.html" target="_blank"><span class="dot"></span>Workspace Link 1 (103)</a>
        <a class="link-card" href="https://10.128.245.138:8443/ui/ad/v1/index.html" target="_blank"><span class="dot"></span>Workspace Link 2 (10)</a>
        <a class="link-card" href="https://helpdesk.aforeserve.co.in/" target="_blank"><span class="dot"></span>Monitor Ticket Logging</a>
        <a class="link-card" href="https://forms.office.com/pages/responsepage.aspx?id=KAt9XPi9DEGqk03zcrFiA4fdXVSLOTFDhvE87_lA3nBUMjBXVFlKS1VXVFlQMlc5SDg1N1JLQ1VYNi4u&route=shorturl" target="_blank"><span class="dot"></span>Resolve &#8211; Billable Lead</a>
        <a class="link-card" href="https://lenovo-plrs-uat.crm5.dynamics.com/" target="_blank"><span class="dot"></span>MSD UAT</a>
        <a class="link-card" href="https://lenovo-plrs-prod.crm5.dynamics.com/" target="_blank"><span class="dot"></span>MSD PROD</a>
        <a class="link-card" href="https://download.lenovo.com/bsco/index.html" target="_blank"><span class="dot"></span>BIOS Simulator Center</a>
        <a class="link-card" href="http://csp.lenovo.com/ibinapp/il/Login.jsp" target="_blank"><span class="dot"></span>CSP</a>
      </div>
    </div>

    <!-- LEARNING & DEVELOPMENT -->
    <div class="panel" id="learning">
      <div class="panel-title">&#127891; Learning and Development</div>
      <div class="card-row">
        <div class="info-card">
          <h3>LEAP</h3>
          <div class="domain">apps.bsharpcorp.com</div>
          <p>Click Here to access LEAP, where you will find all learning modules related to products, diagnostics, and other essential topics.</p>
          <a class="btn" href="https://apps.bsharpcorp.com/" target="_blank">Open LEAP &#8599;</a>
        </div>
        <div class="info-card">
          <h3>UKM</h3>
          <div class="domain">ukm.lenovo.com</div>
          <p>Click here to access UKM, which provides all known tips, the Problem Determination Guide, and various additional resources.</p>
          <a class="btn" href="https://ukm.lenovo.com/" target="_blank">Open UKM &#8599;</a>
        </div>
        <div class="info-card">
          <h3>Communicare</h3>
          <div class="domain">lenovoind-my.sharepoint.com</div>
          <p>Access Call Script, Call Disclaimers and Phonetics documents. Please let us know if anything is required to be included.</p>
          <a class="btn" href="https://lenovoind-my.sharepoint.com/:f:/r/personal/mpintoo_lenovo_com/Documents/One%20Pager/Communicare?csf=1&web=1&e=s5LdaE" target="_blank">Open Communicare &#8599;</a>
        </div>
      </div>
    </div>

    <!-- PROCESS DOCUMENTS -->
    <div class="panel" id="process-docs">
      <div class="panel-title">&#128193; Process Documents</div>
      <div class="doc-grid">
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:t:/g/personal/mpintoo_lenovo_com/IQB_yvlRXUWDSI6_9Ugrwd7qAbVIkFNE9jSQ6bYxopHLKGw?e=b7VEpb" data-type="word" data-name="Case Template">
          <span class="pill-icon">&#128221;</span>Case Template
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:b:/g/personal/mpintoo_lenovo_com/IQAalfwa-QbxTo6BTUw-GlwZAfutGFAdPRazc34PFKbI3yA?e=4d9mQB" data-type="pdf" data-name="CEC Call Logging Process">
          <span class="pill-icon">&#128196;</span>CEC Call Logging Process
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQAWtzQPy-V9T4sHaR0tpv-mAbF7jQcoq9TYk6PcKuV8IXs?e=IQJegN" data-type="excel" data-name="Remote &amp; Rescue Guide">
          <span class="pill-icon">&#128202;</span>Remote &amp; Rescue Guide
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:t:/g/personal/mpintoo_lenovo_com/IQD2ujAlc69HTbc-c_GfVbSfAa1a0V8HBDNi_w44fPGyqPQ?e=yGQPGK" data-type="word" data-name="Service Delivery Instruction">
          <span class="pill-icon">&#128221;</span>Service Delivery Instruction
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQCQKdSxst1RQpI12zczcoSTAaAScDRX7OZl8Pi-44DFHN0?e=fNyvCv" data-type="excel" data-name="RRR Selection Guide in WO">
          <span class="pill-icon">&#128202;</span>RRR Selection Guide in WO
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQDXlepyUdUnQ44nI2Ae4mX8AXVRNA6jSjxU2lBLOAGEMq4?e=9IqHR9" data-type="excel" data-name="Windows Reset &amp; OSRI Guide">
          <span class="pill-icon">&#128202;</span>Windows Reset &amp; OSRI Guide
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:t:/g/personal/mpintoo_lenovo_com/IQDhJdns8NWLRpHNASUyb-TrAZp-S6o2BiWJkAvespudg-g?e=db5mDu" data-type="word" data-name="Shipping Instructions">
          <span class="pill-icon">&#128221;</span>Shipping Instructions
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQCT406A9M6zRo-rvQfUfCd0AY4wnYYaxrS0IshO2rGPdp4?e=xO0oyt" data-type="excel" data-name="HCS Code">
          <span class="pill-icon">&#128202;</span>HCS Code
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:f:/g/personal/mpintoo_lenovo_com/IgBYdvNPCnMNQ5001O6T1AyLAbgJOU9KpMaEYKlzAIsqPjY?e=LdnUL2" data-type="link" data-name="Consumer Accessory Details">
          <span class="pill-icon">&#128193;</span>Consumer Accessory Details
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQCbBdj6ADpoSJdbJzYzw102AcJJmV5WPDwH825TGA3ioHk?e=4qOToW" data-type="excel" data-name="LFR &amp; LES Partner List">
          <span class="pill-icon">&#128202;</span>LFR &amp; LES Partner List
        </span>
        <span class="doc-pill" data-href="https://support.lenovo.com/in/en/solutions/ht035306-lcd-display-pixel-policy-idealenovo-laptops-and-tablets" data-type="link" data-name="Dead Pixel Policy">
          <span class="pill-icon">&#128279;</span>Dead Pixel Policy
        </span>
        <span class="doc-pill" data-href="https://download.lenovo.com/lenovo/lsw/adp_sa_en_in_think.pdf" data-type="pdf" data-name="ADP Terms (Commercial)">
          <span class="pill-icon">&#128196;</span>ADP Terms (Commercial)
        </span>
        <span class="doc-pill" data-href="https://download.lenovo.com/lenovo/lsw/adp_sa_en_in_idea.pdf" data-type="pdf" data-name="ADP Terms (Consumer)">
          <span class="pill-icon">&#128196;</span>ADP Terms (Consumer)
        </span>
        <span class="doc-pill" data-href="https://download.lenovo.com/pccbbs/thinkcentre_pdf/l505-0010-03_en_update.pdf" data-type="pdf" data-name="Lenovo Limited Warranty Terms">
          <span class="pill-icon">&#128196;</span>Lenovo Limited Warranty Terms
        </span>
        <span class="doc-pill" data-href="https://support.lenovo.com/kn/en/solutions/ht505335" data-type="link" data-name="IWS Terms">
          <span class="pill-icon">&#128279;</span>IWS Terms
        </span>
      </div>
    </div>

    <!-- CONTACT NUMBERS -->
    <div class="panel" id="contact">
      <div class="panel-title">&#128222; Contact Numbers</div>
      <div class="phone-grid">
        <div class="phone-block">
          <h3>Toll Free Number</h3>
          <ul>
            <li><strong>Commercial</strong><span>1800-419-4666 / 1800-121-8465</span></li>
            <li><strong>Consumer</strong><span>1800-419-7555 / 1800-121-5366</span></li>
            <li><strong>Premium Care</strong><span>1800-121-9339</span></li>
            <li><strong>Premier Support</strong><span>1800-419-9339</span></li>
            <li><strong>MBG (Smartphone)</strong><span>1800-419-6686</span></li>
            <li><strong>Tablet</strong><span>1800-208-7555</span></li>
            <li><strong>Workstation</strong><span>1800-121-7225</span></li>
            <li><strong>Post Sales</strong><span>1800-572-6465</span></li>
            <li><strong>Sales</strong><span>1800-4199-733</span></li>
            <li><strong>Moto book</strong><span>18004196686</span></li>
            <li><strong>Fujitsu</strong><span>1800-891-2273</span></li>
            <li><strong>Server</strong><span>+91 80 6884 6800</span></li>
          </ul>
        </div>
        <div class="phone-block">
          <h3>Direct Transfer Number</h3>
          <ul>
            <li><strong>Commercial</strong><span>12409</span></li>
            <li><strong>Consumer</strong><span>12428</span></li>
            <li><strong>Premium Care</strong><span>12421</span></li>
            <li><strong>Premier Support</strong><span>12419</span></li>
            <li><strong>MBG (Smartphone)</strong><span>13440</span></li>
            <li><strong>Tablet</strong><span>12429</span></li>
            <li><strong>Workstation</strong><span>12415</span></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- J2W URLs -->
    <div class="panel" id="j2w">
      <div class="panel-title">&#9889; J2W URLs <small style="font-size:0.78rem;font-weight:400;color:#666;margin-left:8px;">Joules to Watts &#8212; Time Matters</small></div>
      <div class="link-grid" style="max-width:480px;">
        <a class="link-card" href="https://apiv2.trackervigil.com/Account/Login?ReturnUrl=/connect/authorize/callback?client_id%3Detms-web.app%26redirect_uri%3Dhttps%253A%252F%252Fj2w.trackervigil.com%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520offline_access%26state%3D85c2bad31f3a41ac8f91ddb73a7953c1%26code_challenge%3Dx5ovYtpxb0b4YTOj9d-EBABAYbIx7XS4XwXVp-yHYds%26code_challenge_method%3DS256%26acr_values%3Dtenant%253Aj2w%26response_mode%3Dquery%26host%3Dhttps%253A%252F%252Fj2w" target="_blank"><span class="dot"></span>Transport &#8211; Trackervigil</a>
        <a class="link-card" href="https://j2wlenovo.greythr.com/v3/portal/ess/home" target="_blank"><span class="dot"></span>Attendance Marking</a>
      </div>
    </div>

    <!-- OUR COMMUNITY -->
    <div class="panel" id="community">
      <div class="panel-title">&#127760; Our Community</div>
      <div class="social-grid">
        <a class="social-card" href="https://www.facebook.com/LenovoIndia/" target="_blank">
          <div class="social-icon fb">f</div><span>Lenovo India &#8211; Facebook</span>
        </a>
        <a class="social-card" href="https://www.instagram.com/lenovo_india/" target="_blank">
          <div class="social-icon ig">&#128248;</div><span>@lenovo_india &#8211; Instagram</span>
        </a>
        <a class="social-card" href="https://www.youtube.com/user/lenovoindia" target="_blank">
          <div class="social-icon yt">&#9654;</div><span>Lenovo India &#8211; YouTube</span>
        </a>
        <a class="social-card" href="https://x.com/Lenovo_in" target="_blank">
          <div class="social-icon tw">&#120143;</div><span>@Lenovo_in &#8211; X (Twitter)</span>
        </a>
        <a class="social-card" href="https://in.linkedin.com/company/lenovoin" target="_blank">
          <div class="social-icon li">in</div><span>Lenovo India &#8211; LinkedIn</span>
        </a>
      </div>
    </div>

    <!-- MDOA CRITERIA CHECK -->
    <div class="panel" id="mdoa">
      <div class="panel-title">&#128203; MDOA Criteria Check</div>
      <div class="mdoa-form">

        <div class="mdoa-hint">
          <b>How to use:</b> Enter the Case Created Date from your file as the Start Date.
          Enter today's or reference date as End Date. Type the partner name to auto-detect LFR / Non-LFR.
        </div>

        <div class="mdoa-field">
          <label>Start Date <span>*</span> <small>(Case Created Date from file)</small></label>
          <input type="date" id="mdoaStart" class="mdoa-input" />
        </div>

        <div class="mdoa-field">
          <label>End Date <span>*</span></label>
          <input type="date" id="mdoaEnd" class="mdoa-input" />
        </div>

        <div class="mdoa-field">
          <label>Partner / Customer Name <span>*</span></label>
          <input type="text" id="mdoaPartner" class="mdoa-input"
                 placeholder="e.g. Croma, Vijay Sales, Reliance Digital..." />
        </div>

        <button class="mdoa-btn" onclick="calculateMDOA()">&#128200; Calculate</button>

        <div class="mdoa-result" id="mdoaResult"></div>

      </div>
    </div>

    <!-- FEEDBACK -->
    <div class="panel" id="feedback">
      <div class="panel-title">&#128172; Help Us Improve Together</div>
      <div class="feedback-box">
        <div>
          <h2>Help Us Improve Together</h2>
          <p>Your insights help us build a better workplace &#8212; share your thoughts with us.</p>
        </div>
        <a href="https://forms.office.com/r/iMgYfdaFmh" target="_blank">Submit Your Feedback</a>
      </div>
    </div>

  </div><!-- /content-panel -->
</div><!-- /main-wrapper -->

<footer>
  IT Helpdesk Home &bull; IN CEC Training Team &bull; Published 5/5/2026
</footer>

<script>
  let currentPanelId = 'lenovo-urls';

  document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
      const target = item.dataset.target;
      currentPanelId = target;
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      item.classList.add('active');
      closeFileViewer(false);
      document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
      document.getElementById(target).classList.add('active');
    });
  });

  function getFileType(href, explicitType) {
    if (explicitType && explicitType !== 'link') return explicitType;
    if (href.includes('/:x:/')) return 'excel';
    if (href.includes('/:t:/')) return 'word';
    if (href.includes('/:b:/')) return 'pdf';
    const path = href.split('?')[0].toLowerCase();
    if (path.endsWith('.xlsx') || path.endsWith('.xls') || path.endsWith('.csv')) return 'excel';
    if (path.endsWith('.docx') || path.endsWith('.doc')) return 'word';
    if (path.endsWith('.pdf')) return 'pdf';
    if (path.endsWith('.txt')) return 'text';
    return 'link';
  }

  const badgeConfig = {
    excel: { label: 'Excel', cls: 'badge-excel' },
    word:  { label: 'Word',  cls: 'badge-word'  },
    pdf:   { label: 'PDF',   cls: 'badge-pdf'   },
    text:  { label: 'Text',  cls: 'badge-text'  },
  };

  function buildEmbedUrl(href, type) {
    // Only called for non-SharePoint embeddable files (public PDFs, etc.)
    return href;
  }

  function openFileViewer(href, name, type) {
    const cfg = badgeConfig[type] || { label: type.toUpperCase(), cls: 'badge-text' };
    document.getElementById('viewer-badge').textContent = cfg.label;
    document.getElementById('viewer-badge').className   = 'file-type-badge ' + cfg.cls;
    document.getElementById('viewer-title').textContent = name;
    document.getElementById('viewer-newtab').href       = href;
    document.getElementById('viewer-frame').src         = buildEmbedUrl(href, type);
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    document.getElementById('file-viewer').classList.add('active');
  }

  function closeFileViewer(restorePanel = true) {
    document.getElementById('file-viewer').classList.remove('active');
    document.getElementById('viewer-frame').src = '';
    if (restorePanel) document.getElementById(currentPanelId).classList.add('active');
  }

  // ── MDOA Criteria Check ───────────────────────────────────────────────────
  var LFR_KEYWORDS = [
    'croma','woolworths wholesale','infiniti wholesale','infiniti retail',
    'future value retail','pantaloons retail','home solutions retail','ezone',
    'reliance digital','reliance hypermart',
    'jumbo electronics',
    'lotus electronics','cpr distributors',
    'vijay sales',
    'pai international',
    'bajaj electronics',
    'vivek limited',
    'lulu hypermarket'
  ];
  var MDOA_HOLIDAYS = [
    [1,1],[15,1],[26,1],[19,3],[1,5],
    [14,9],[2,10],[21,10],[10,11],[25,12]
  ];
  function mdoaIsHoliday(d){
    return MDOA_HOLIDAYS.some(function(h){ return d.getDate()===h[0] && d.getMonth()+1===h[1]; });
  }
  function mdoaIsWeekend(d){ var day=d.getDay(); return day===0||day===6; }
  function mdoaIsWorking(d){ return !mdoaIsWeekend(d) && !mdoaIsHoliday(d); }
  function mdoaWorkingDays(start,end){
    var count=0, cur=new Date(start);
    cur.setDate(cur.getDate()+1);
    var endD=new Date(end);
    while(cur<=endD){ if(mdoaIsWorking(cur)) count++; cur.setDate(cur.getDate()+1); }
    return count;
  }
  function mdoaIsLFR(name){
    var n=name.toLowerCase();
    return LFR_KEYWORDS.some(function(k){ return n.indexOf(k)>-1; });
  }
  function calculateMDOA(){
    var sv=document.getElementById('mdoaStart').value;
    var ev=document.getElementById('mdoaEnd').value;
    var pv=document.getElementById('mdoaPartner').value.trim();
    var res=document.getElementById('mdoaResult');
    if(!sv||!ev||!pv){
      res.style.display='block'; res.className='mdoa-error';
      res.innerHTML='&#9888; Please fill in all three fields.'; return;
    }
    var start=new Date(sv), end=new Date(ev);
    if(end<start){
      res.style.display='block'; res.className='mdoa-error';
      res.innerHTML='&#9888; Entered date is older than the invoice date.'; return;
    }
    var days=mdoaWorkingDays(start,end);
    var isLFR=mdoaIsLFR(pv);
    var type=isLFR?'LFR':'Non-LFR';
    var limit=isLFR?15:7;
    var ok=days<=limit;
    var label=ok?('Its Within '+limit+' day'):('Its Not Within '+limit+' day');
    var col=ok?'#22c55e':'#ef4444';
    var bg=ok?'rgba(34,197,94,0.1)':'rgba(239,68,68,0.1)';
    var brd=ok?'rgba(34,197,94,0.3)':'rgba(239,68,68,0.3)';
    res.style.display='block';
    res.className='mdoa-result';
    res.style.background=bg; res.style.border='1px solid '+brd;
    res.innerHTML=
      '<div class="mdoa-result-label">MDOA Result</div>'
      +'<div class="mdoa-result-grid">'
      +'<div class="mdoa-result-cell"><small>Type</small><strong>'+type+'</strong></div>'
      +'<div class="mdoa-result-cell"><small>Working Days</small><strong>'+days+' days</strong></div>'
      +'<div class="mdoa-result-cell highlight"><small>Result</small>'
      +'<strong style="color:'+col+';">'+label+'</strong></div>'
      +'</div>';
  }
  // ─────────────────────────────────────────────────────────────────────────

  document.querySelectorAll('.doc-pill[data-href]').forEach(pill => {
    pill.addEventListener('click', () => {
      const href = pill.dataset.href;
      const name = pill.dataset.name;
      const type = getFileType(href, pill.dataset.type);

      // SharePoint / OneDrive enforce X-Frame-Options: SAMEORIGIN —
      // they refuse to load inside any iframe.  Open in a new tab instead
      // (the browser already has the user's auth session there).
      if (href.includes('sharepoint.com') || type === 'link') {
        window.open(href, '_blank');
        return;
      }

      // Public files (e.g. download.lenovo.com PDFs) can be embedded inline.
      openFileViewer(href, name, type);
    });
  });
</script>

</body>
</html>"""


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                         STREAMLIT APP                                   ║
# ╚══════════════════════════════════════════════════════════════════════════╝

st.set_page_config(
    page_title            = "Lenovo One Pager",
    page_icon             = "🔴",
    layout                = "wide",
    initial_sidebar_state = "collapsed",
)

# ── Global CSS: hide Streamlit chrome on every page ─────────────────────────
st.markdown("""
<style>
    #MainMenu, header, footer               { display: none !important; height: 0 !important; }
    [data-testid="stHeader"]               { display: none !important; height: 0 !important; }
    [data-testid="stAppViewContainer"]     { padding-top: 0 !important; }
    section[data-testid="stMain"]          { padding-top: 0 !important; }
    .stAppHeader, .st-emotion-cache-uf99v8 { display: none !important; height: 0 !important; }
    .stApp                                  { margin: 0 !important; padding: 0 !important;
                                            background:
                                              radial-gradient(circle at 15% 45%, rgba(160,18,18,0.75) 0%, transparent 45%),
                                              radial-gradient(circle at 80% 85%, rgba(10,12,80,0.85)  0%, transparent 42%),
                                              radial-gradient(circle at 65% 18%, rgba(130,10,130,0.5) 0%, transparent 40%),
                                              radial-gradient(circle at 48% 62%, rgba(95,10,155,0.6)  0%, transparent 50%),
                                              radial-gradient(circle at 90% 30%, rgba(60,0,120,0.55)  0%, transparent 35%),
                                              linear-gradient(135deg, #5c0808 0%, #4a0a6e 48%, #0d0b3e 100%) !important; }
    .block-container                        { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
    [data-testid="stToolbar"]               { display: none !important; }
    [data-testid="stDecoration"]            { display: none !important; }
    [data-testid="stStatusWidget"]          { display: none !important; }
    [data-testid="stToolbarActions"]        { display: none !important; }
    [data-testid="stAppToolbar"]            { display: none !important; }
    .stDeployButton                         { display: none !important; }
    .viewerBadge_container__r5tak          { display: none !important; }
    #stDecoration                           { display: none !important; }
    .st-emotion-cache-h4xjcd               { display: none !important; }
    button[title="Manage app"]              { display: none !important; }
    button[aria-label="Manage app"]         { display: none !important; }
    [data-testid="stBottom"]                { display: none !important; }
    .stBottomBlockContainer                 { display: none !important; }
    [class*="bottom"]                       { display: none !important; }
    [data-testid="stSidebar"]               { display: none !important; }
    iframe                                  { border: none !important; display: block; margin: 0 !important; padding: 0 !important; }
    [data-testid="stVerticalBlock"]         { gap: 0 !important; }
    [data-testid="stVerticalBlock"] > div   { margin: 0 !important; padding: 0 !important; }
    [data-testid="stMainBlockContainer"]    { gap: 0 !important; padding: 0 !important; }
    [data-testid="stHorizontalBlock"]       { gap: 0 !important; margin-bottom: 0 !important; }

    /* Login page styles */
    .login-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        background: linear-gradient(135deg, #0a0a23 0%, #1a1a4e 50%, #2d0036 100%);
        padding: 40px 20px;
    }
    .login-box {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px;
        padding: 48px 44px;
        width: 100%;
        max-width: 420px;
        text-align: center;
    }
    .login-box h1 {
        font-size: 1.6rem;
        font-weight: 900;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #fff;
        margin-bottom: 6px;
    }
    .login-box p  { color: #999; font-size: 0.88rem; margin-bottom: 28px; }
    .login-badge  {
        display: inline-block;
        background: #e50000;
        color: #fff;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 20px;
    }

    /* Override Streamlit input/button styles for login */
    div[data-testid="stTextInput"] input {
        background: #ffffff !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 8px !important;
        color: #111111 !important;
        font-size: 0.9rem !important;
        padding: 12px 14px !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #e50000 !important;
        box-shadow: 0 0 0 2px rgba(229,0,0,0.25) !important;
    }
    div[data-testid="stTextInput"] label { color: #aaa !important; font-size: 0.82rem !important; }
    div[data-testid="stForm"] { border: none !important; padding: 0 !important; }

    button[kind="primaryFormSubmit"],
    button[kind="primary"] {
        background: #e50000 !important;
        border: none !important;
        border-radius: 8px !important;
        font-size: 0.9rem !important;
        font-weight: 700 !important;
        padding: 12px !important;
        width: 100% !important;
        margin-top: 8px !important;
    }
    button[kind="primaryFormSubmit"]:hover,
    button[kind="primary"]:hover {
        background: #b30000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Hide "Manage app" toolbar injected by Streamlit Cloud
st.markdown("""
<img src="x" onerror="
(function(){
  function hide(){
    document.querySelectorAll('button,a,[role=button]').forEach(function(el){
      if(el.innerText && el.innerText.trim()==='Manage app'){
        var p=el;
        for(var i=0;i<6;i++){
          p.style.setProperty('display','none','important');
          if(p.parentElement) p=p.parentElement; else break;
        }
      }
    });
    var bottom=document.querySelector('[data-testid=stBottom]');
    if(bottom) bottom.style.setProperty('display','none','important');
  }
  hide();
  setInterval(hide,800);
  new MutationObserver(hide).observe(document.body,{childList:true,subtree:true});
})();
" style="display:none" />
""", unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  LOGIN GATE — require Lenovo ID before showing the dashboard            ║
# ╚══════════════════════════════════════════════════════════════════════════╝

if "lenovo_id" not in st.session_state or not st.session_state["lenovo_id"]:

    # Top-right label — no highlight, plain text
    st.markdown("""
    <div style="position:fixed;top:12px;right:20px;
                color:#aaa;font-size:0.72rem;letter-spacing:0.5px;
                z-index:9999;">
        Introduced by India CEC Training Team
    </div>
    """, unsafe_allow_html=True)

    # Centre the form on the page
    _, mid, _ = st.columns([1, 2, 1])

    with mid:
        st.markdown("""
        <div style="height:160px"></div>
        <div style="text-align:center;">
            <h1 style="font-size:1.7rem;font-weight:900;letter-spacing:3px;
                       text-transform:uppercase;color:#fff;
                       text-shadow:0 2px 16px rgba(229,0,0,0.4);margin-bottom:6px;
                       text-align:center;width:100%;display:block;">
                Lenovo One Pager
            </h1>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            lenovo_id = st.text_input(
                "Lenovo ID",
                placeholder="e.g. jsmith@lenovo.com",
                help="Enter your official Lenovo email address"
            )
            submitted = st.form_submit_button("Continue →", use_container_width=True, type="primary")

        if submitted:
            val = lenovo_id.strip().lower()
            if not val:
                st.error("Please enter your Lenovo ID to continue.")
            elif val not in ALLOWED_USERS:
                st.error("Access denied — your email is not on the authorised list.")
            else:
                st.session_state["lenovo_id"] = val
                st.session_state["lenovo_name"] = ALLOWED_USERS[val]
                st.rerun()


    st.stop()   # ← don't render dashboard until logged in


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  DASHBOARD — shown after successful Lenovo ID entry                     ║
# ╚══════════════════════════════════════════════════════════════════════════╝

# ── Top bar: Title (left)  |  Welcome + Logout (right) ─────────────────────
name = st.session_state.get("lenovo_name", st.session_state["lenovo_id"])

st.markdown("""
<style>
  /* Dark branded header row */
  [data-testid="stHorizontalBlock"]:first-of-type {
    background: linear-gradient(135deg, #0a0a23 0%, #1a1a4e 55%, #2d0036 100%);
    border-bottom: 3px solid #e50000;
    padding: 4px 24px !important;
    margin: 0 !important;
    align-items: center !important;
  }
  /* Power-off button */
  [data-testid="stHorizontalBlock"]:first-of-type button {
    width: 38px !important;
    height: 38px !important;
    min-height: unset !important;
    padding: 0 !important;
    border-radius: 50% !important;
    background: rgba(229,0,0,0.15) !important;
    border: 2px solid #e50000 !important;
    color: #e50000 !important;
    font-size: 1.1rem !important;
    line-height: 1 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background 0.2s, box-shadow 0.2s !important;
    box-shadow: 0 0 8px rgba(229,0,0,0.3) !important;
  }
  [data-testid="stHorizontalBlock"]:first-of-type button:hover {
    background: #e50000 !important;
    color: #fff !important;
    box-shadow: 0 0 16px rgba(229,0,0,0.7) !important;
  }
</style>
""", unsafe_allow_html=True)

col_title, col_welcome, col_logout = st.columns([6, 2.5, 1])

with col_title:
    st.markdown("""
    <div style="padding:8px 0 12px 0;">
      <div style="font-size:1.3rem;font-weight:900;letter-spacing:3px;
                  text-transform:uppercase;color:#fff;
                  text-shadow:0 2px 14px rgba(229,0,0,0.45);">
        Lenovo One Pager
      </div>
      <div style="font-size:0.71rem;color:#888;margin-top:3px;letter-spacing:0.5px;">
        Introduced by the IN CEC Training Team
      </div>
    </div>""", unsafe_allow_html=True)

with col_welcome:
    st.markdown(
        f"<div style='padding:10px 8px 0 0;text-align:right;"
        f"color:#aaa;font-size:0.82rem;'>"
        f"&#128100; Welcome, <b style='color:#fff'>{name}</b></div>",
        unsafe_allow_html=True
    )

with col_logout:
    st.markdown("<div style='padding:4px 0 0 0'></div>", unsafe_allow_html=True)
    if st.button("⏻", use_container_width=False, help="Logout"):
        st.session_state.pop("lenovo_id", None)
        st.session_state.pop("lenovo_name", None)
        st.rerun()

# ── Render the full HTML dashboard ──────────────────────────────────────────
# height uses JS to detect viewport; fallback is 900px
components.html(
    HTML_CONTENT + """
    <script>
      // Tell Streamlit iframe to resize to full window height
      function setHeight() {
        const h = window.innerHeight || document.documentElement.clientHeight || 850;
        window.frameElement && (window.frameElement.style.height = h + 'px');
      }
      setHeight();
      window.addEventListener('resize', setHeight);
    </script>
    """,
    height=870,
    scrolling=False,
)
