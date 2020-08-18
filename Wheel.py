"""db wheel
"""
import re

class Wheel:
    def __init__(self, partno, oracle, size, et, pcd, cb, color, drill, qty):
        self.partno = partno
        self.oracle = oracle
        self.size = size 
        self.et = et
        self.pcd = pcd
        self.cb = cb
        self.color = color
        self.drill = drill
        self.qty = qty

    '''match bpmet to pcd
    '''
    def isPcd(self, bpmet):
        if bpmet == self.pcd:
            return True
        return False

    '''match hub to cb 
    '''
    def isCb(self, hub):
        try:
            # sample hub1: 66.56 
            r1 = re.compile('[0-9]+\.[0-9]+')
            # sample hub2: 66
            r2 = re.compile('[0-9]+')

            # sample hub3: F-57.1/R-66.56
            r3 = re.compile('[A-Z]-[0-9]+\.[0-9]+/[A-Z]-[0-9]+\.[0-9]+')

            # hub1
            if hub is not None and (r1.match(hub) or r2.match(hub)) and float(self.cb) >= float(hub):
                return True
            # hub2
            elif hub is not None and r3.match(hub):
                arr1 = hub.split('/', 1)
                arr2 = arr1[0].split('-', 1)
                arr3 = arr1[1].split('-', 1)
                front = float(arr2[1])
                rear = float(arr3[1])
                # print('front: ' + str(front) + '     Rear: ' + str(rear))
                final_hub = max(front, rear)
                # print(final_hub)
                if float(self.cb) > float(final_hub):
                    return True 
        except ValueError:
            print('ValueError at isPcd')
            return False
        return False

    '''match offsetmm to et
    '''
    def isEt(self, offsetmm):
        # example offsetmm: 40-50
        r = re.compile('.*.*-.*.*')
        if offsetmm is not None and r.match(offsetmm) is not None:
            # sample offsetmm: '35-45'
            # split offset into min and max
            arr = offsetmm.split('-', 1)
            #before the hyphen -
            offsetmm_min = arr[0]
            # after the hypen - 
            offsetmm_max = arr[1]
            if float(self.et) <= float(offsetmm_max) and float(self.et) >= float(offsetmm_min):
                return True
        return False

    '''match tiresize(n) to size
    '''
    def isSize(self, wheelsize):
        # sample tiresize: '215/45-17'
        if(wheelsize is not None):
            # PSG wheel
            try:
                # sample tiresize: 215/45-17
                arr1 = wheelsize.split('/', 1)
                arr2 = arr1[1].split('-', 1)
                wheel_diam_in = int(arr2[1])
                psg_diameter = float(wheel_diam_in)

                # standard wheel
                arr3 = self.size.split('x', 1)
                diameter = float(arr3[0])
                # width = float(arr3[1])

                if psg_diameter == diameter:
                    return True

            except ValueError:
                print('Value error in isSize')
                return False
        return False
    
    # def isSize2(self, min_width, max_width, min_diameter, max_diameter):
    #     # standard wheel
    #     arr3 = self.size.split('x', 1)
    #     diameter = float(arr3[0])
    #     width = float(arr3[1])

    #     if (width >= min_width and width <= max_width and diameter >= min_diameter and diameter <= max_diameter):
    #         return True
    #     return False
    
    # match tiresize(n) to size



    