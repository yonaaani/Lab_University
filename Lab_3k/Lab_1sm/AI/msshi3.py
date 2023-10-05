import numpy as np

#[0, 0, 0, 0, 0, 0, 0, 0,  # Х'
 #0, 0, 0, 0, 0, 0, 0, 0,
 #0, 0, 0, 0, 0, 0, 0, 0,
 #0, 0, 0, 0, 0, 0, 0, 0,
 #0, 0, 0, 0, 0, 0, 0, 0,
 #0, 0, 0, 0, 0, 0, 0, 0,
 #0, 0, 0, 0, 0, 0, 0, 0],

# Вхідні дані (вхідні вектори для кожної букви)
X = np.array([[0, 0, 1, 1, 1, 1, 0, 0,  # 'А'
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0],

              [0, 1, 1, 1, 1, 1, 1, 0,  # 'Б'
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 1, 1, 1, 1, 0, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0],
              
              [0, 1, 1, 1, 1, 1, 0, 0,  # 'В'
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0],
              
              [0, 1, 1, 1, 1, 1, 1, 0,  # 'Г'
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0],
              
              [0, 1, 1, 1, 1, 1, 1, 0,  # 'Д'
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 1, 0,
               1, 0, 0, 0, 0, 0, 0, 1,
               1, 0, 0, 0, 0, 0, 0, 1],
              
              [0, 1, 1, 1, 1, 1, 1, 0,  # 'Е'
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 1, 1, 1, 1, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 1, 1, 1, 1, 1, 0],
              
              [0, 0, 0, 1, 1, 1, 1, 0,  # 'Є'
               0, 0, 1, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 1, 1, 1, 1, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 0, 1, 0, 0, 0, 0, 0,
               0, 0, 0, 1, 1, 1, 1, 0],
              
              [1, 0, 0, 1, 1, 0, 0, 1,  # 'Ж'
               0, 1, 0, 1, 1, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0,
               1, 1, 1, 1, 1, 1, 1, 1,
               0, 0, 1, 1, 1, 1, 0, 0,
               0, 1, 0, 1, 1, 0, 1, 0,
               1, 0, 0, 1, 1, 0, 0, 1],
              
              [0, 1, 1, 1, 1, 1, 0, 0,  # 'З'
               0, 0, 0, 0, 0, 0, 1, 0,
               0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0,
               0, 0, 0, 0, 0, 0, 1, 0,
               0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0],
              
              [0, 1, 0, 0, 0, 0, 1, 0,  # 'И'
               0, 1, 0, 0, 0, 1, 1, 0,
               0, 1, 0, 0, 0, 1, 1, 0,
               0, 1, 0, 0, 1, 0, 1, 0,
               0, 1, 0, 1, 0, 0, 1, 0,
               0, 1, 1, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0],
              
              [0, 0, 0, 1, 1, 0, 0, 0,  # 'І'
               0, 0, 0, 1, 1, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0],
              
              [0, 0, 1, 0, 0, 1, 0, 0,  # 'Ї'
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 0, 0],
              
             [0, 1, 0, 1, 1, 0, 1, 0,  # 'Й'
              0, 1, 0, 0, 0, 1, 1, 0,
              0, 1, 0, 0, 0, 1, 1, 0,
              0, 1, 0, 0, 1, 0, 1, 0,
              0, 1, 0, 1, 0, 0, 1, 0,
              0, 1, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0],
             
             [0, 1, 0, 0, 0, 1, 0, 0,  # 'К'
              0, 1, 0, 0, 1, 0, 0, 0,
              0, 1, 0, 1, 0, 0, 0, 0,
              0, 1, 1, 0, 0, 0, 0, 0,
              0, 1, 0, 1, 0, 0, 0, 0,
              0, 1, 0, 0, 1, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 0, 0],
             
             [0, 0, 0, 0, 1, 1, 1, 0,  # 'Л'
              0, 0, 0, 1, 0, 0, 1, 0,
              0, 0, 0, 1, 0, 0, 1, 0,
              0, 0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0],
             
             [0, 1, 0, 0, 0, 0, 1, 0,  # 'М'
              0, 1, 1, 0, 0, 1, 1, 0,
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0],
             
             [0, 1, 0, 0, 0, 0, 1, 0,  # 'Н'
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0],
             
             [0, 0, 1, 1, 1, 1, 0, 0,  # 'О'
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 1, 0, 0],
             
             [0, 1, 1, 1, 1, 1, 1, 0,  # 'П'
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0],
             
             [0, 1, 1, 1, 1, 0, 0, 0,  # Р'
              0, 1, 0, 0, 0, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0, 0,
              0, 1, 1, 1, 1, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0, 0],
             
             [0, 0, 0, 1, 1, 0, 0, 0,  # C'
              0, 0, 1, 0, 0, 1, 0, 0,
              0, 1, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 0, 0, 0, 0, 0,
              0, 0, 0, 1, 1, 1, 0, 0],
             
             [0, 1, 1, 1, 1, 1, 1, 0,  # T'
              0, 0, 0, 1, 1, 0, 0, 0,
              0, 0, 0, 1, 1, 0, 0, 0,
              0, 0, 0, 1, 1, 0, 0, 0,
              0, 0, 0, 1, 1, 0, 0, 0,
              0, 0, 0, 1, 1, 0, 0, 0,
              0, 0, 0, 1, 1, 0, 0, 0],
             
             [0, 1, 0, 0, 0, 0, 1, 0,  # У'
              0, 0, 1, 0, 0, 1, 0, 0,
              0, 0, 0, 1, 1, 0, 0, 0,
              0, 0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 0, 1, 0, 0, 0,
              0, 0, 1, 1, 0, 0, 0, 0],
             
             [0, 0, 0, 1, 1, 0, 0, 0,  # Ф'
              0, 1, 1, 1, 1, 1, 1, 0,
              1, 0, 0, 1, 1, 0, 0, 1,
              1, 0, 0, 1, 1, 0, 0, 1,
              0, 1, 1, 1, 1, 1, 1, 0,
              0, 0, 0, 1, 1, 0, 0, 0,
              0, 0, 0, 1, 1, 0, 0, 0],
             
             [1, 0, 0, 0, 0, 0, 0, 1,  # Х'
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 0, 1, 0, 0, 1, 0, 0,
              0, 0, 0, 1, 1, 0, 0, 0,
              0, 0, 1, 0, 0, 1, 0, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              1, 0, 0, 0, 0, 0, 0, 1],
             
             [0, 1, 0, 0, 0, 0, 1, 0,  # Ц'
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 1, 1, 1,
              0, 0, 0, 0, 0, 0, 0, 1],
             
             [0, 1, 0, 0, 0, 0, 1, 0,  # Ч'
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 1, 1, 0,
              0, 0, 0, 0, 0, 0, 1, 0,
              0, 0, 0, 0, 0, 0, 1, 0,
              0, 0, 0, 0, 0, 0, 1, 0],
             
             [0, 1, 0, 1, 1, 0, 1, 0,  # Ш'
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 1, 1, 1, 1, 1, 0],
             
             [0, 1, 0, 1, 1, 0, 1, 0,  # Щ'
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 0, 1, 1, 0, 1, 0,
              0, 1, 1, 1, 1, 1, 1, 1,
              0, 0, 0, 0, 0, 0, 0, 1],
             
             [0, 1, 0, 0, 0, 0, 0, 0,  # Ь'
              0, 1, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0, 0,
              0, 1, 1, 1, 1, 0, 0, 0],
             
             [0, 1, 0, 0, 1, 1, 1, 0,  # Ю'
              0, 1, 0, 1, 0, 0, 0, 1,
              0, 1, 0, 1, 0, 0, 0, 1,
              0, 1, 1, 1, 0, 0, 0, 1,
              0, 1, 0, 1, 0, 0, 0, 1,
              0, 1, 0, 1, 0, 0, 0, 1,
              0, 1, 0, 0, 1, 1, 1, 0],
             
             [0, 0, 0, 0, 1, 1, 1, 0,  # Я'
              0, 0, 0, 1, 0, 0, 1, 0,
              0, 0, 0, 1, 0, 0, 1, 0,
              0, 0, 0, 1, 0, 0, 1, 0,
              0, 0, 0, 0, 1, 1, 1, 0,
              0, 0, 0, 0, 0, 1, 1, 0,
              0, 0, 0, 0, 1, 0, 1, 0]
             
             ])

# Вихідні дані (бажані відповіді для кожної букви)
desired_outputs = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'А'
                            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Б'
                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'В'
                            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Г'
                            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Д'
                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Е'
                            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Є'
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Ж'
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'З'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'И'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'І'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Ї'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Й'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'К'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Л'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'М'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Н'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'О'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'П'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Р'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'С'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Т'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'У'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Ф'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 'Х'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 'Ц'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 'Ч'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 'Ш'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 'Щ'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 'Ь'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 'Ю'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]  # 'Я'
                            ])  

# Ініціалізація вагових коефіцієнтів зі зміненою розмірністю
np.random.seed(1)
synaptic_weights = 0.01 * np.random.randn(56, 32)  # Змінена розмірність вагових коефіцієнтів і використання нормального розподілу

# Коефіцієнт швидкості навчання
learning_rate = 0.001

# Кількість ітерацій для навчання (збільшена кількість ітерацій)
epochs = 1000

# Лічильник для кількості ітерацій
iteration_counter = 0

# Навчання персептрона
for epoch in range(epochs):
    for i in range(len(X)):
        # Прямий прохід
        input_layer = X[i]
        output = np.dot(input_layer, synaptic_weights)
        
        # Визначення активації (поріг)
        activation = (output > 0).astype(int)
        
        # Різниця між бажаним виходом і фактичним виходом
        error = desired_outputs[i] - activation
        
        # Оновлення вагових коефіцієнтів і нейронного зміщення
        delta_weights = learning_rate * np.outer(input_layer, error)
        synaptic_weights += delta_weights

        # Інкрементуємо лічильник ітерацій
        iteration_counter += 1

    # Якщо мережа досягла великої точності, можна завершити навчання раніше
    if np.mean(np.abs(error)) < 0.01:
        print(f"Навчання завершено після {iteration_counter} ітерацій")
        break

# Функція для розпізнавання букви та виводу відповідних даних
def recognize_letter(letter):
    if letter in 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ':
        letter_index = ord(letter) - ord('А')  # Індекс букви у матриці
        input_test = X[letter_index]
        output_test = np.dot(input_test, synaptic_weights)
        weights_for_letter = synaptic_weights[:, letter_index]
        bias_for_letter = synaptic_weights[-1, letter_index]  # Останній рядок - нейронне зміщення

        # Округлюємо вихід та ваги до 4 знаків після коми
        activation = output_test > 0
        weights_rounded = np.round(weights_for_letter, 4)
        bias_rounded = np.round(bias_for_letter, 4)

        print(f"Дані для букви {letter}:")
        print("Вихід:")
        print(activation.astype(int))
        print("Ваги:")
        print(weights_rounded)
        print("Нейронне зміщення:")
        print(bias_rounded)
    else:
        print("Буква не розпізнана. Введіть одну з літер АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ.")

# Введення користувача
user_input = input("Введіть одну букву: ")
recognize_letter(user_input.upper())  # Перетворення на великі літери для однорідності
