
temperaturas = [
     [   "Chone"
         [   "Semana 1"
            {"dia": "Lunes", "temp": 31},
            {"dia": "Martes", "temp": 31},
            {"dia": "Miércoles", "temp": 31},
            {"dia": "Jueves", "temp": 30},
            {"dia": "Viernes", "temp": 30},
            {"dia": "Sábado", "temp": 31},
            {"dia": "Domingo", "temp": 30} 
        ],
        [   "Semana 2"
            {"dia": "Lunes", "temp": 31},
            {"dia": "Martes", "temp": 33},
            {"dia": "Miércoles", "temp": 33},
            {"dia": "Jueves", "temp": 33},
            {"dia": "Viernes", "temp": 31},
            {"dia": "Sábado", "temp": 30},
            {"dia": "Domingo", "temp": 30}
        ],
        [   "Semana 3"
            {"dia": "Lunes", "temp": 30},
            {"dia": "Martes", "temp": 31},
            {"dia": "Miércoles", "temp": 31},
            {"dia": "Jueves", "temp": 31},
            {"dia": "Viernes", "temp": 31},
            {"dia": "Sábado", "temp": 32},
            {"dia": "Domingo", "temp": 31}
        ],
        [   "Semana 4"
            {"dia": "Lunes", "temp": 31},
            {"dia": "Martes", "temp": 29},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 29},
            {"dia": "Viernes", "temp": 31},
            {"dia": "Sábado", "temp": 30},
            {"dia": "Domingo", "temp": 30}
        ]
    ],
    [   "Quito"
        [   "Semana 1"
            {"dia": "Lunes", "temp": 18},
            {"dia": "Martes", "temp": 18},
            {"dia": "Miércoles", "temp": 19},
            {"dia": "Jueves", "temp": 20},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 19}
        ],
        [   "Semana 2"
            {"dia": "Lunes", "temp": 16},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 20},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 16}
        ],
        [   'Semana 3'
            {"dia": "Lunes", "temp": 16},
            {"dia": "Martes", "temp": 16},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 16},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 15},
            {"dia": "Domingo", "temp": 15}
        ],
        [   "Semana 4"
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 16},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 15},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 15},
            {"dia": "Domingo", "temp": 16}
        ]
    ],
    [   "Guayaquill"
        [   "Semana 1"
            {"dia": "Lunes", "temp": 33},
            {"dia": "Martes", "temp": 33},
            {"dia": "Miércoles", "temp": 33},
            {"dia": "Jueves", "temp": 33},
            {"dia": "Viernes", "temp": 32},
            {"dia": "Sábado", "temp": 33},
            {"dia": "Domingo", "temp": 32}
        ],
        [   "Semana 2"
            {"dia": "Lunes", "temp": 33},
            {"dia": "Martes", "temp": 35},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 32},
            {"dia": "Viernes", "temp": 33},
            {"dia": "Sábado", "temp": 32},
            {"dia": "Domingo", "temp": 35}
        ],
        [   "Semana 3"
            {"dia": "Lunes", "temp": 33},
            {"dia": "Martes", "temp": 34},
            {"dia": "Miércoles", "temp": 34},
            {"dia": "Jueves", "temp": 35},
            {"dia": "Viernes", "temp": 34},
            {"dia": "Sábado", "temp": 33},
            {"dia": "Domingo", "temp": 34}
        ],
        [   "Semana 4"
            {"dia": "Lunes", "temp": 33},
            {"dia": "Martes", "temp": 32},
            {"dia": "Miércoles", "temp": 34},
            {"dia": "Jueves", "temp": 34},
            {"dia": "Viernes", "temp": 34},
            {"dia": "Sábado", "temp": 34},
            {"dia": "Domingo", "temp": 34}
        ]
    ]
]


ciudades = ["Chone", "Quito", "Guayaquill"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
