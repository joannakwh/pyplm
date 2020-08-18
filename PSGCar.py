"""Plussizeguide car
"""
class PSGCar:
    # constructor
    def __init__(self, 
        year,
        make,
        model,
        bpmet,
        hub,
        offsetmm,
        wheelsize1,
        tiresize1,
        wheelsize2,
        tiresize2,
        wheelsize3,
        tiresize3,
        wheelsize4,
        tiresize4,
        wheelsize5,
        tiresize5,
        wheelsize6,
        tiresize6,
        wheelsize7,
        tiresize7,
        wheelsize8,
        tiresize8,
        wheelsize9,
        tiresize9,
        wheelsize10,
        tiresize10,
        wheelsize11,
        tiresize11,
        ):
        
        self.year = year
        self.make = make
        self.model = model
        self.bpmet = bpmet
        self.hub = hub
        self.offsetmm = offsetmm
        # self.min_width = None
        # self.max_width = None
        # self.min_diameter = None
        # self.max_diameter = None

        # initialize wheel and tire sizes into a dict
        self.sizes = {}
        # self.widths = []
        # self.diameters = []

        if (wheelsize1 and tiresize1) is not None: 
            self.sizes[wheelsize1] = tiresize1
            #print(self.sizes[wheelsize1])
        
        if (wheelsize2 and tiresize2) is not None: 
            self.sizes[wheelsize2] = tiresize2
            #print(self.sizes[wheelsize2])
        
        if (wheelsize3 and tiresize3) is not None: 
            self.sizes[wheelsize3] = tiresize3
            #print(self.sizes[wheelsize3])

        if (wheelsize4 and tiresize4) is not None: 
            self.sizes[wheelsize4] = tiresize4
            #print(self.sizes[wheelsize4])

        if (wheelsize5 and tiresize5) is not None: 
            self.sizes[wheelsize5] = tiresize5
            #print(self.sizes[wheelsize5])

        if (wheelsize6 and tiresize6) is not None: 
            self.sizes[wheelsize6] = tiresize6
            #print(self.sizes[wheelsize6])

        if (wheelsize7 and tiresize7) is not None: 
            self.sizes[wheelsize7] = tiresize7
            #print(self.sizes[wheelsize7])

        if wheelsize8 and tiresize8 is not None: 
            self.sizes[wheelsize8] = tiresize8
            #print(self.sizes[wheelsize8])

        if wheelsize9 and tiresize9 is not None: 
            self.sizes[wheelsize9] = tiresize9
            #print(self.sizes[wheelsize9])

        if wheelsize10 and tiresize10 is not None: 
            self.sizes[wheelsize10] = tiresize10
            #print(self.sizes[wheelsize10])

        if wheelsize11 and tiresize11 is not None: 
            self.sizes[wheelsize11] = tiresize11
            #print(self.sizes[wheelsize11])

        # calculate all widths and diameters
        
        # width and diameter calculation
        # for i in self.sizes:
        #     arr1 = self.sizes[i].split('/', 1)
        #     wheel_width_mm = int(arr1[0])
        #     arr2 = arr1[1].split('-', 1)
        #     aspect_ratio = int(arr2[0])
        #     wheel_diam_in = int(arr2[1])
        #     width = float(wheel_width_mm / 25.4)
        #     #diameter = float(wheel_width_mm * aspect_ratio / 2540 + wheel_diam_in)
        #     diameter = float(wheel_diam_in)
        #     self.widths.append(width)
        #     self.diameters.append(diameter)


        # find max and min width and diameter
        # self.max_width = self.widths[0]
        # self.min_width = self.widths[0]
        # self.max_diameter = self.diameters[0]
        # self.min_diameter = self.diameters[0]

        # for width in self.widths:
        #     if width > self.max_width:
        #         self.max_width = width
        #     if width < self.min_width:
        #         self.min_width = width
        # for diameter in self.diameters:
        #     if diameter > self.max_diameter:
        #         self.max_diameter = diameter
        #     if diameter < self.min_diameter:
        #         self.min_diameter = diameter
        # print('')
        # print('Min tire width: ' + str(round(float(self.min_width), 1)) + '     ' + 'Max tire width: ' + str(round(float(self.max_width), 1)))
        # print('Min tire diameter: ' + str(round(float(self.min_diameter), 1)) + '     ' + 'Max tire diameter: ' + str(round(float(self.max_diameter), 1)))
        # print('')

    
# x = PSGCar('2020','ACURA', 'MDX', '5x120', '64.1', '35-45', 'OE-18', '245/60-18', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

    

        




    