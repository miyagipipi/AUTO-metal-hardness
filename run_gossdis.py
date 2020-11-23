import gossdis_ver2 as gs

if __name__ == '__main__':
    print('请输入硬度标准和范围，目前可选的有HRC(59-64)，HRC(22-34)，HRB(60-110)。\n')
    print('正确的输入格式为：HRA79_85，HRC22_34和HRC59_64')

    hardnessName = input('请输入： ')
    nums = int(input('需要多少组数据： ')) * 3

    if hardnessName == 'HRA79_85':
        #(self, mean, div, _max, _min, nums)
        
        res = gs.metalHardness(82.5, 0.840112, 84, 79.5, nums)
        res.HRA79_85()

    elif hardnessName == 'HRC22_34':
        
        res = gs.metalHardness(24.9, 4.361664, 30.4, 22.0, nums)
        res.HRC22_34()

    elif hardnessName == 'HRC59_64':
        res = gs.metalHardness(61.7, 1.08, 63.9, 59.0, nums)

    
