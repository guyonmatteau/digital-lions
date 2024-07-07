interface ApiResponse {
  first_name: string;
  last_name: string;
  id: number;
}

const fetchData = async (): Promise<ApiResponse[]> => {
try {
  // const response = await fetch('https://backend-production-7bbc.up.railway.app/api/v1/communities', {
  //   method: 'GET',
  //   headers: {
  //     'Content-Type': 'application/json'
  //   }
  // });
  // console.log('Data:', response.json());
  // if (!response.ok) {
  //   throw new Error(`Error: ${response.statusText}`);
  // }
  // const data: ApiResponse[] = await response.json();
  // return data;
  const   response = [
    {
      "first_name": "Zibuyile",
      "last_name": "Bhensela",
      "id": 1
    },
    {
      "first_name": "Lungile",
      "last_name": "Mkhabela",
      "id": 2
    },
    {
      "first_name": "Thandeka",
      "last_name": "Sangweni",
      "id": 3
    },
    {
      "first_name": "Mnqobi",
      "last_name": "Andile",
      "id": 4
    },
    {
      "first_name": "Jabulani",
      "last_name": "Gcwabe",
      "id": 5
    },
    {
      "first_name": "Thandazile",
      "last_name": "Mpanza",
      "id": 6
    },
    {
      "first_name": "Thembisile",
      "last_name": "Gxabhashe",
      "id": 7
    },
    {
      "first_name": "Nomathemba",
      "last_name": "Dinabantu",
      "id": 8
    },
    {
      "first_name": "Musa",
      "last_name": "Gedeza",
      "id": 9
    },
    {
      "first_name": "Nhlanhla",
      "last_name": "Nonduma",
      "id": 10
    },
    {
      "first_name": "Thandiwe",
      "last_name": "Thumbela",
      "id": 11
    },
    {
      "first_name": "Busisiwe",
      "last_name": "Maphindela",
      "id": 12
    },
    {
      "first_name": "Siyabonga",
      "last_name": "Nkosi",
      "id": 13
    },
    {
      "first_name": "Andile",
      "last_name": "Shange",
      "id": 14
    },
    {
      "first_name": "Olwethu",
      "last_name": "Juqula",
      "id": 15
    },
    {
      "first_name": "Thandeka",
      "last_name": "Khaphela",
      "id": 16
    },
    {
      "first_name": "Mnqobi",
      "last_name": "Mbonambi",
      "id": 17
    },
    {
      "first_name": "Thandiwe",
      "last_name": "Nxele",
      "id": 18
    },
    {
      "first_name": "Lungile",
      "last_name": "Shoba",
      "id": 19
    },
    {
      "first_name": "Nomagugu",
      "last_name": "Mbongwa",
      "id": 20
    },
    {
      "first_name": "Nonhlanhla",
      "last_name": "Shazi",
      "id": 21
    },
    {
      "first_name": "Nomthandazo",
      "last_name": "Mazalankosi",
      "id": 22
    },
    {
      "first_name": "Sibusiso",
      "last_name": "Mthalane",
      "id": 23
    },
    {
      "first_name": "Luyanda",
      "last_name": "Madondo",
      "id": 24
    },
    {
      "first_name": "Nhlanhla",
      "last_name": "Mahlalela",
      "id": 25
    },
    {
      "first_name": "Thalente",
      "last_name": "Gwagwa",
      "id": 26
    },
    {
      "first_name": "Nomalanga",
      "last_name": "Somboni",
      "id": 27
    },
    {
      "first_name": "Mthokozisi",
      "last_name": "Nkumane",
      "id": 28
    },
    {
      "first_name": "Thalente",
      "last_name": "Nkamzwayo",
      "id": 29
    },
    {
      "first_name": "Vusumuzi",
      "last_name": "Shelembe",
      "id": 30
    },
    {
      "first_name": "Minenhle",
      "last_name": "Ndiyema",
      "id": 31
    },
    {
      "first_name": "Thalente",
      "last_name": "Bophela",
      "id": 32
    },
    {
      "first_name": "Dumisani",
      "last_name": "Shibase",
      "id": 33
    },
    {
      "first_name": "Lungile",
      "last_name": "Mkhabela",
      "id": 34
    },
    {
      "first_name": "Andile",
      "last_name": "Dlakela",
      "id": 35
    },
    {
      "first_name": "Lwandile",
      "last_name": "Vangisa",
      "id": 36
    },
    {
      "first_name": "Nozizwe",
      "last_name": "Maphanga",
      "id": 37
    },
    {
      "first_name": "Jabulani",
      "last_name": "Msweli",
      "id": 38
    },
    {
      "first_name": "Nomthandazo",
      "last_name": "Sikhosana",
      "id": 39
    },
    {
      "first_name": "Musa",
      "last_name": "Mncwabe",
      "id": 40
    },
    {
      "first_name": "Andile",
      "last_name": "Mahlase",
      "id": 41
    },
    {
      "first_name": "Thabisile",
      "last_name": "Miya",
      "id": 42
    },
    {
      "first_name": "Thabani",
      "last_name": "Phuthini",
      "id": 43
    },
    {
      "first_name": "Bandile",
      "last_name": "Khezokhulu",
      "id": 44
    },
    {
      "first_name": "Njabulo",
      "last_name": "Mavuso",
      "id": 45
    },
    {
      "first_name": "Bhekani",
      "last_name": "Mafobo",
      "id": 46
    },
    {
      "first_name": "Mcebisi",
      "last_name": "Mfeka",
      "id": 47
    },
    {
      "first_name": "Nqobizitha",
      "last_name": "Mathibela",
      "id": 48
    },
    {
      "first_name": "Thabani",
      "last_name": "Dube",
      "id": 49
    },
    {
      "first_name": "Mandla",
      "last_name": "Caluza",
      "id": 50
    },
    {
      "first_name": "Thembile",
      "last_name": "Vezi",
      "id": 51
    },
    {
      "first_name": "Minenhle",
      "last_name": "Nyazitla",
      "id": 52
    },
    {
      "first_name": "Thabisile",
      "last_name": "Masina",
      "id": 53
    },
    {
      "first_name": "SimphiweyiNkosi",
      "last_name": "Mphankomo",
      "id": 54
    },
    {
      "first_name": "Lungile",
      "last_name": "Gigaba",
      "id": 55
    },
    {
      "first_name": "Busisiwe",
      "last_name": "Mbongwa",
      "id": 56
    },
    {
      "first_name": "Zinhle",
      "last_name": "Mntimande",
      "id": 57
    },
    {
      "first_name": "Sandile",
      "last_name": "Sokhulu",
      "id": 58
    },
    {
      "first_name": "Busisiwe",
      "last_name": "Sikhunyana",
      "id": 59
    },
    {
      "first_name": "Thabisa",
      "last_name": "Dube",
      "id": 60
    },
    {
      "first_name": "Mzamo",
      "last_name": "Nyembezi",
      "id": 61
    },
    {
      "first_name": "Nomathalente",
      "last_name": "Msweli",
      "id": 62
    },
    {
      "first_name": "Sibonelo",
      "last_name": "Mphemba",
      "id": 63
    },
    {
      "first_name": "Olwethu",
      "last_name": "Gadlela",
      "id": 64
    },
    {
      "first_name": "Nobuhle",
      "last_name": "Nkamzwayo",
      "id": 65
    },
    {
      "first_name": "Sibongile",
      "last_name": "Mkhonza",
      "id": 66
    },
    {
      "first_name": "Sithembiso",
      "last_name": "Nonkululeko",
      "id": 67
    },
    {
      "first_name": "Minenhle",
      "last_name": "Sigagu",
      "id": 68
    },
    {
      "first_name": "Musa",
      "last_name": "Mjoli",
      "id": 69
    },
    {
      "first_name": "Nobuhle",
      "last_name": "Gxabhashe",
      "id": 70
    },
    {
      "first_name": "Nomathalente",
      "last_name": "Mjwara",
      "id": 71
    },
    {
      "first_name": "Thabisa",
      "last_name": "Sokhwebula",
      "id": 72
    },
    {
      "first_name": "Bhekani",
      "last_name": "Vezi",
      "id": 73
    },
    {
      "first_name": "Thandeka",
      "last_name": "Phoseka",
      "id": 74
    },
    {
      "first_name": "Andile",
      "last_name": "Gasela",
      "id": 75
    },
    {
      "first_name": "Musa",
      "last_name": "Mngwemkhulu",
      "id": 76
    },
    {
      "first_name": "Vusumuzi",
      "last_name": "Gubhela",
      "id": 77
    },
    {
      "first_name": "Busisiwe",
      "last_name": "Phakathi",
      "id": 78
    },
    {
      "first_name": "Minenhle",
      "last_name": "Nsukuza",
      "id": 79
    },
    {
      "first_name": "Thembekile",
      "last_name": "Nhlanhla",
      "id": 80
    },
    {
      "first_name": "Mthokozisi",
      "last_name": "Manana",
      "id": 81
    },
    {
      "first_name": "Lwandile",
      "last_name": "Dlakela",
      "id": 82
    },
    {
      "first_name": "Nomagugu",
      "last_name": "Mbuyisa",
      "id": 83
    },
    {
      "first_name": "Nomthandazo",
      "last_name": "Madonsela",
      "id": 84
    },
    {
      "first_name": "Nkazimulo",
      "last_name": "Nzimase",
      "id": 85
    },
    {
      "first_name": "Bhekisisa",
      "last_name": "Mdladla",
      "id": 86
    },
    {
      "first_name": "Mandla",
      "last_name": "Fakazi",
      "id": 87
    },
    {
      "first_name": "Thembisile",
      "last_name": "Mshazi",
      "id": 88
    },
    {
      "first_name": "Mlungisi",
      "last_name": "Thusini",
      "id": 89
    },
    {
      "first_name": "Nomathalente",
      "last_name": "Majozi",
      "id": 90
    },
    {
      "first_name": "Siphesihle",
      "last_name": "Thembekwayo",
      "id": 91
    },
    {
      "first_name": "Njabulo",
      "last_name": "Ngungunyana",
      "id": 92
    },
    {
      "first_name": "Gugu",
      "last_name": "Mboyisa",
      "id": 93
    },
    {
      "first_name": "Bhekokwakhe",
      "last_name": "Dlebenkomo",
      "id": 94
    },
    {
      "first_name": "Luyanda",
      "last_name": "Mbuli",
      "id": 95
    },
    {
      "first_name": "Bhekokwakhe",
      "last_name": "Mbeje",
      "id": 96
    },
    {
      "first_name": "Mzamo",
      "last_name": "Mtolo",
      "id": 97
    },
    {
      "first_name": "S'fiso",
      "last_name": "Bukhosini",
      "id": 98
    },
    {
      "first_name": "Luyanda",
      "last_name": "Guliwe",
      "id": 99
    },
    {
      "first_name": "Nonhlanhla",
      "last_name": "Mlungisi",
      "id": 100
    },
    {
      "first_name": "Nomalanga",
      "last_name": "Nkwaliyenkosi",
      "id": 101
    },
    {
      "first_name": "Thandiwe",
      "last_name": "Chamane",
      "id": 102
    },
    {
      "first_name": "Nobantu",
      "last_name": "Nhlanhla",
      "id": 103
    },
    {
      "first_name": "S'fiso",
      "last_name": "Langa",
      "id": 104
    },
    {
      "first_name": "Siphesihle",
      "last_name": "Zikhungwini",
      "id": 105
    },
    {
      "first_name": "Njabulo",
      "last_name": "Khuba",
      "id": 106
    },
    {
      "first_name": "Siphesihle",
      "last_name": "Nodlomo",
      "id": 107
    },
    {
      "first_name": "Mzamo",
      "last_name": "Gxabhashe",
      "id": 108
    },
    {
      "first_name": "Nomcebo",
      "last_name": "Gxabhashe",
      "id": 109
    },
    {
      "first_name": "S'fiso",
      "last_name": "Nyawokhulu",
      "id": 110
    },
    {
      "first_name": "Nomalanga",
      "last_name": "Mkhokeleleki",
      "id": 111
    },
    {
      "first_name": "Sibusiso",
      "last_name": "Zikhungwini",
      "id": 112
    },
    {
      "first_name": "Dumisani",
      "last_name": "Mncwanga",
      "id": 113
    },
    {
      "first_name": "Thandeka",
      "last_name": "Madiba",
      "id": 114
    },
    {
      "first_name": "Nkazimulo",
      "last_name": "Lutholoni",
      "id": 115
    },
    {
      "first_name": "Luyanda",
      "last_name": "Ngema",
      "id": 116
    },
    {
      "first_name": "Sibusisiwe",
      "last_name": "Makhulukhulu",
      "id": 117
    },
    {
      "first_name": "SimphiweyiNkosi",
      "last_name": "Mtumaseli",
      "id": 118
    },
    {
      "first_name": "Mcebisi",
      "last_name": "Magujwa",
      "id": 119
    },
    {
      "first_name": "Vusumuzi",
      "last_name": "Cebisa",
      "id": 120
    },
    {
      "first_name": "Thabani",
      "last_name": "Mcambi",
      "id": 121
    },
    {
      "first_name": "Noxolo",
      "last_name": "Hlongwane",
      "id": 122
    },
    {
      "first_name": "Thalente",
      "last_name": "Mbunjwa",
      "id": 123
    },
    {
      "first_name": "Silondile",
      "last_name": "Bantwini",
      "id": 124
    },
    {
      "first_name": "Mcebisi",
      "last_name": "Mbungela",
      "id": 125
    },
    {
      "first_name": "Simphiwe",
      "last_name": "Lembede",
      "id": 126
    },
    {
      "first_name": "Thalente",
      "last_name": "Ndabansele",
      "id": 127
    },
    {
      "first_name": "Sihawukele",
      "last_name": "Hangala",
      "id": 128
    },
    {
      "first_name": "Thuthukile",
      "last_name": "Dlangamandla",
      "id": 129
    },
    {
      "first_name": "Thabisile",
      "last_name": "Mkhabela",
      "id": 130
    },
    {
      "first_name": "Silondile",
      "last_name": "Ntenga",
      "id": 131
    },
    {
      "first_name": "Sibusisiwe",
      "last_name": "Maseko",
      "id": 132
    },
    {
      "first_name": "Sihawukele",
      "last_name": "Ncwaba",
      "id": 133
    },
    {
      "first_name": "Mandla",
      "last_name": "Ndandali",
      "id": 134
    },
    {
      "first_name": "Thabisa",
      "last_name": "Mayisela",
      "id": 135
    },
    {
      "first_name": "Gugulethu",
      "last_name": "Gwamanda",
      "id": 136
    },
    {
      "first_name": "Vusumuzi",
      "last_name": "Sengwayo",
      "id": 137
    },
    {
      "first_name": "Njabulo",
      "last_name": "Mabizela",
      "id": 138
    },
    {
      "first_name": "Mlungisi",
      "last_name": "Nxasana",
      "id": 139
    },
    {
      "first_name": "Nozizwe",
      "last_name": "Hlabisa",
      "id": 140
    },
    {
      "first_name": "Lwandile",
      "last_name": "Mabhodla",
      "id": 141
    },
    {
      "first_name": "Thembile",
      "last_name": "Shibase",
      "id": 142
    },
    {
      "first_name": "Luyanda",
      "last_name": "Nkwakha",
      "id": 143
    },
    {
      "first_name": "Thandeka",
      "last_name": "Dlawuza",
      "id": 144
    },
    {
      "first_name": "Nokulunga",
      "last_name": "Mtshali",
      "id": 145
    },
    {
      "first_name": "Nonjabulo",
      "last_name": "Mshengu",
      "id": 146
    },
    {
      "first_name": "Nokulunga",
      "last_name": "Shozi",
      "id": 147
    },
    {
      "first_name": "Thabisa",
      "last_name": "Mthembu",
      "id": 148
    },
    {
      "first_name": "Nqobizitha",
      "last_name": "Mthonti",
      "id": 149
    },
    {
      "first_name": "Langalibalele",
      "last_name": "Msweli",
      "id": 150
    },
    {
      "first_name": "Mcebisi",
      "last_name": "Mpungose",
      "id": 151
    },
    {
      "first_name": "Luyanda",
      "last_name": "Nkomose",
      "id": 152
    },
    {
      "first_name": "Nomathemba",
      "last_name": "Dinabantu",
      "id": 153
    },
    {
      "first_name": "Thalente",
      "last_name": "Hlela",
      "id": 154
    },
    {
      "first_name": "Mcebisi",
      "last_name": "Mgasela",
      "id": 155
    },
    {
      "first_name": "Langalibalele",
      "last_name": "Mpangazitha",
      "id": 156
    },
    {
      "first_name": "Siyabonga",
      "last_name": "Kholose",
      "id": 157
    },
    {
      "first_name": "Mandla",
      "last_name": "Dlodlo",
      "id": 158
    },
    {
      "first_name": "Nobantu",
      "last_name": "Mthembu",
      "id": 159
    },
    {
      "first_name": "Noxolo",
      "last_name": "Mbatha",
      "id": 160
    },
    {
      "first_name": "Sihawukele",
      "last_name": "Khuluse",
      "id": 161
    },
    {
      "first_name": "Jabulani",
      "last_name": "Nyawo",
      "id": 162
    },
    {
      "first_name": "Mandlakhe",
      "last_name": "Sangweni",
      "id": 163
    },
    {
      "first_name": "Mcebisi",
      "last_name": "Nzama",
      "id": 164
    },
    {
      "first_name": "Bandile",
      "last_name": "Juqula",
      "id": 165
    },
    {
      "first_name": "Nonhlanhla",
      "last_name": "Mkhonza",
      "id": 166
    },
    {
      "first_name": "Sandile",
      "last_name": "Amahle",
      "id": 167
    },
    {
      "first_name": "Nozibusiso",
      "last_name": "Maphalala",
      "id": 168
    },
    {
      "first_name": "Mthokozisi",
      "last_name": "Sibindi",
      "id": 169
    },
    {
      "first_name": "Nhlanhla",
      "last_name": "Mhayise",
      "id": 171
    },
    {
      "first_name": "Vusumuzi",
      "last_name": "Madiba",
      "id": 172
    },
    {
      "first_name": "Musa",
      "last_name": "Gedeza",
      "id": 173
    },
    {
      "first_name": "Mzamo",
      "last_name": "Jamile",
      "id": 174
    },
    {
      "first_name": "Thembisile",
      "last_name": "Khawula",
      "id": 175
    },
    {
      "first_name": "Nokulunga",
      "last_name": "Mabika",
      "id": 176
    },
    {
      "first_name": "Jabulani",
      "last_name": "Khathini",
      "id": 177
    },
    {
      "first_name": "Thembekile",
      "last_name": "Manzi",
      "id": 178
    },
    {
      "first_name": "Thabani",
      "last_name": "Thembekwayo",
      "id": 179
    },
    {
      "first_name": "Thembile",
      "last_name": "Khathi",
      "id": 180
    },
    {
      "first_name": "Amahle",
      "last_name": "Bhembe",
      "id": 181
    },
    {
      "first_name": "Bhekizizwe",
      "last_name": "Vilakazi",
      "id": 182
    },
    {
      "first_name": "Sibongile",
      "last_name": "Nombela",
      "id": 183
    },
    {
      "first_name": "Thabani",
      "last_name": "Chibi",
      "id": 184
    },
    {
      "first_name": "Nomvula",
      "last_name": "Mzoneli",
      "id": 185
    },
    {
      "first_name": "Thandiwe",
      "last_name": "Dingila",
      "id": 186
    },
    {
      "first_name": "Mthokozisi",
      "last_name": "Mangena",
      "id": 187
    },
    {
      "first_name": "Nomcebo",
      "last_name": "Gubeshe",
      "id": 188
    },
    {
      "first_name": "Bhekizizwe",
      "last_name": "Khumalo",
      "id": 189
    },
    {
      "first_name": "Londisizwe",
      "last_name": "Mnangwe",
      "id": 190
    },
    {
      "first_name": "Thembile",
      "last_name": "Gubhuza",
      "id": 191
    },
    {
      "first_name": "Zinhle",
      "last_name": "Ngcemu",
      "id": 192
    },
    {
      "first_name": "Nhlanhla",
      "last_name": "Nonduma",
      "id": 193
    },
    {
      "first_name": "Langalibalele",
      "last_name": "Meyiwa",
      "id": 194
    },
    {
      "first_name": "Nobantu",
      "last_name": "Chonco",
      "id": 195
    },
    {
      "first_name": "Andile",
      "last_name": "Nontanda",
      "id": 196
    },
    {
      "first_name": "Mlungisi",
      "last_name": "Dlebenkomo",
      "id": 197
    },
    {
      "first_name": "Londisizwe",
      "last_name": "Gengeshe",
      "id": 198
    },
    {
      "first_name": "Bhekisisa",
      "last_name": "Dludla",
      "id": 199
    },
    {
      "first_name": "Thandeka",
      "last_name": "Nzama",
      "id": 200
    },
    {
      "first_name": "Nozizwe",
      "last_name": "Mchunu",
      "id": 201
    },
    {
      "first_name": "Nkazimulo",
      "last_name": "Cebekhulu",
      "id": 202
    },
    {
      "first_name": "Nomusa",
      "last_name": "Mlungisi",
      "id": 203
    },
    {
      "first_name": "Mcebisi",
      "last_name": "Ngema",
      "id": 204
    },
    {
      "first_name": "Gugulethu",
      "last_name": "Jili",
      "id": 205
    },
    {
      "first_name": "Nothando",
      "last_name": "Mphephethwa",
      "id": 206
    },
    {
      "first_name": "Sithembiso",
      "last_name": "Hlomuka",
      "id": 207
    },
    {
      "first_name": "Nomvula",
      "last_name": "Yei",
      "id": 208
    },
    {
      "first_name": "Siyabonga",
      "last_name": "Phoswa",
      "id": 209
    },
    {
      "first_name": "Nomathalente",
      "last_name": "Gubhuza",
      "id": 210
    },
    {
      "first_name": "Zenzile",
      "last_name": "Mshengu",
      "id": 170
    }
  ]
  return response
} catch (error) {
  console.error('Error fetching data:', error);
  throw error;
}
};

export default fetchData;
