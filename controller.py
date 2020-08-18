import os.path
import PSGCar as PSGCar
import pandas as pd
from xlrd import open_workbook
import Wheel
    
def match(info, path):
    matches = []
    car = PSGCar.PSGCar(info.get('YEAR'), info.get('MAKE'), info.get('MODEL'), info.get('BPMET'), info.get('HUB'), info.get('OFFSETMM'),
        info.get('WHEELSIZE1'), info.get('TIRESIZE1'),
        info.get('WHEELSIZE2'), info.get('TIRESIZE2'), 
        info.get('WHEELSIZE3'), info.get('TIRESIZE3'),
        info.get('WHEELSIZE4'), info.get('TIRESIZE4'),
        info.get('WHEELSIZE5'), info.get('TIRESIZE5'), 
        info.get('WHEELSIZE6'), info.get('TIRESIZE6'), 
        info.get('WHEELSIZE7'), info.get('TIRESIZE7'), 
        info.get('WHEELSIZE8'), info.get('TIRESIZE8'),
        info.get('WHEELSIZE9'), info.get('TIRESIZE9'),
        info.get('WHEELSIZE10'), info.get('TIRESIZE10'),
        info.get('WHEELSIZE11'), info.get('TIRESIZE11'))

    wb = open_workbook('C:/Users/Cloudlin/Desktop/WheelSTK2.xlsx')
    sheet = wb.sheet_by_name('stock')
    number_of_rows = sheet.nrows
    number_of_columns = 9
    count = 0

    # add wheels from spreadsheet
    wheels = []
    for row in range(1, number_of_rows):
        values=[]
        for col in range(number_of_columns):
            value = (sheet.cell(row,col).value)
            try:
                str(int(value))
                if len(str(value)) <= 0:
                    break
            except ValueError:
                pass
            finally:
                values.append(value)
        if len(values) == 9:
            count = count + 1
            # print(values)
            wheel = Wheel.Wheel(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])
            wheels.append(wheel)

    for wheel in wheels:
        # match bolt pattern, hub/cb, offset
        if wheel.isPcd(car.bpmet): 
            print('bpmet match')
            print('wheel: ' + str(wheel.pcd) + ' car: ' + str(car.bpmet))

            # match offset
            if wheel.isEt(car.offsetmm):
                # match tiresize
                print("offset match")
                print('wheel: ' + str(wheel.et) + ' car: ' + str(car.offsetmm))

                # match hub/cb
                if wheel.isCb(car.hub):
                    print('hub match')
                    print('wheel: ' + str(wheel.cb) + ' car: ' + str(car.hub))
                    for wheelsize in car.sizes:
                        if wheel.isSize(car.sizes[wheelsize]):
                            if wheel not in matches: 
                                matches.append(wheel)
                                print('tiresize match')
                                print ('wheel: ' + str(wheel.size) + ' car: ' + str(car.sizes[wheelsize]))
                            
            # print('')
    # print results
    print('')
    print('-----------------------------------------------------------')
    print('MATCHES')
    print('-----------------------------------------------------------')
    print(car.year + ' ' + car.make + ' ' + car.model)
    print('')
    if len(matches) == 0 : print('No matches')
    for match in matches:
        print('PART. NO: ' + str(match.partno))
        print('SIZE: ' + str(match.size))
        print('ET: ' + str(match.et))
        print('PCD: ' + str(match.pcd))
        print('CB: ' + str(match.cb))
        print('COLOR: ' + str(match.color))
        print('QTY: ' + str(int(match.qty)))
        print('')

    # save results to readable .xlsx
    if(len(matches) > 0):
        df1 = pd.DataFrame(columns=['part no.', 'oracle', 'size', 'et', 'PCD', 'CB', 'color', 'drill', 'QTY'])
        for i in range(len(matches)):
            df1.loc[i] = [matches[i].partno, matches[i].oracle, matches[i].size, matches[i].et, matches[i].pcd, matches[i].cb, matches[i].color, matches[i].drill, matches[i].qty]
        print(df1)

        df2 = pd.DataFrame(columns=['YEAR', 'MAKE', 'MODEL', 'BPMET', 'HUB', 'OFFSETMM', 'WHEELSIZE', 'TIRESIZE'])
        df2.loc[0] = [car.year, car.make, car.model, car.bpmet, car.hub, car.offsetmm, '', '']
        df2.loc[1] = ['', '', '', '', '', '', '', '']
        j = 1
        for wheel, tire in car.sizes.items():
            df2.loc[j] = ['', '', '', '', '', '', wheel, tire,]
            j = j + 1
        print(df2)

        outname = str(car.year).replace(' ','_') + '_' + str(car.make).replace(' ','_') + '_' + str(car.model).replace(' ','_') + '.xlsx'
        outdir = './output'
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        fullname = os.path.join(outdir, outname)    
        
        with pd.ExcelWriter(fullname) as writer:  
            df1.to_excel(writer, sheet_name='inventory_matches', index=False)
            df2.to_excel(writer, sheet_name='car_info', index=False)

    

    

    



# checkFile("C:/Users/Cloudlin/Downloads/WheelSTK.xlsx")