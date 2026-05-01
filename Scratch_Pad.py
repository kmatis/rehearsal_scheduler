# -*- coding: utf-8 -*-
class person:
    def __init__(self, name, dates, characters):
        self.name = name
        
        self.dates = dates
        self.cnflct_lst = [date.strip() for date in dates.split(',')]
        
        self.characters = characters
        self.chrctr_lst = [character.strip() for character in characters.split(',')]
   
class month:
    def __init__(self, name, month_num, last_of_month):
        self.name = name
        self.month_num = month_num
        self.first_of_month = 1
        self.last_of_month = last_of_month
        
class scene:
    def __init__(self, name, characters):
        self.name = name
        self.characters = characters
        self.chrctr_lst = [character.strip() for character in characters.split(',')]
        self.num_chrctrs = len(self.chrctr_lst)
        
def name_sort(e):
    return e['name']

Kenneth = person('Kenneth'
                 , '6/12, 6/13, 6/14, 6/15, 6/16, 6/17, 6/18, 6/19, 6/20, 6/21, 6/22, 6/23, 6/24, 6/25, 6/26, 6/27, 6/28, 6/29, 6/30, 7/1'
                 , 'Ophelia, Gravedigger'
                 )

Actor_1  = person('Actor_1'
                  ,'6/20, 6/21, 6/22, 6/23, 6/24, 6/25, 6/26, 6/27, 6/28, 6/29, 6/30, 7/1, 7/2, 7/3, 7/4, 7/5, 7/6, 7/7, 7/8, 7/9, 7/10, 7/11, 7/12, 7/13, 7/14, 7/15'
                  , 'Hamlet'
                  )

Actor_2  = person('Actor_2'
                  ,'7/1, 7/2, 7/3, 7/4, 7/5, 7/6, 7/7, 7/8, 7/9, 7/10, 7/11, 7/12, 7/13, 7/14, 7/15, 7/16, 7/17, 7/18, 7/19, 7/20'
                  , 'Gravedigger2'
                  )

actors = []
actors.append(Kenneth)
actors.append(Actor_1)
actors.append(Actor_2)
actors.sort(key=lambda x: x.name)

June = month('June', 6, 30)
July = month('July', 7, 31)
month_list = []
month_list.append(June)
month_list.append(July)

I_1 = scene(
    'I_1'
    , 'Hamlet, Ophelia'
    )

I_2 = scene(
    'I_2'
    , 'Hamlet, Laeretes, Claudius'
    )
I_3 = scene(
    'I_3'
    , 'Ophelia, Gravedigger, Gravedigger2, Gravedigger3'
    )

I_4 = scene(
    'I_4'
    , 'Gravedigger2'
    )


scene_list = []
scene_list.append(I_1)
scene_list.append(I_2)
scene_list.append(I_3)
scene_list.append(I_4)
scene_list.sort(key=lambda x: x.name)

for scene in scene_list:
    avail_num = 0
    for character in scene.chrctr_lst:
        for actor in actors:
            for act_chrct in actor.chrctr_lst:
                if act_chrct == character:
                    avail_num += 1
     
    avail_perct = avail_num/scene.num_chrctrs
    print(scene.name, " ", "{:.0%}".format(avail_perct))


for month in month_list:
    for i in range(month.first_of_month, month.last_of_month+1):
        
        date_display = ' '.join([month.name, str(i)])
        date = '/'.join([str(month.month_num), str(i)])
        
        avlbl_list = ''
        avlbl_chars = []
        
        print(date_display)
        
        for actor in actors:
            if date not in actor.cnflct_lst:
                for actr_chrt in actor.chrctr_lst:
                    avlbl_chars.append(actr_chrt)
                
                if len(avlbl_list) == 0:
                   avlbl_list = actor.name 
                else:
                    avlbl_list = ', '.join([avlbl_list, actor.name])

    
        if len(avlbl_list) > 0:
            print('    Available actors: ',avlbl_list)   
            
            for scene in scene_list:
                avail_num = 0
                for character in scene.chrctr_lst:
                        for avl_chrct in avlbl_chars:
                            if avl_chrct == character:
                                avail_num += 1
                avail_perct = avail_num/scene.num_chrctrs
                print('    ',scene.name, " ", "{:.0%}".format(avail_perct))
