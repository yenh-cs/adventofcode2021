import numpy as np
import pandas as pd

class CuboidSegment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def to_string(self):
        return '(' + str(self.start) + ',' + str(self.end) + ')'

    def length(self):
        return self.end - self.start + 1

    def is_overlapped(self, another):
        return (self.start >= another.start and another.end >= self.start) or\
                (self.end >= another.start and another.end >= self.end) or\
                (another.start >= self.start and self.end >= another.start) or\
                (another.end >= self.start and self.end >= another.end)
    
    def is_in_valid_range(self, min_value, max_value):
        return (self.start >= min_value and self.end <= max_value)


class Cuboid:
    def init(self, data):
        self.on = data[0]
        self.x = CuboidSegment(data['x'][0], data['x'][1])
        self.y = CuboidSegment(data['y'][0], data['y'][1])
        self.z = CuboidSegment(data['z'][0], data['z'][1])

    def init_with_coordinates(self, coordinates):
        self.on = True
        self.x = CuboidSegment(coordinates[0], coordinates[1])
        self.y = CuboidSegment(coordinates[2], coordinates[3])
        self.z = CuboidSegment(coordinates[4], coordinates[5])

    def clone(self):
        c = Cuboid()
        c.x = CuboidSegment(self.x.start, self.x.end)
        c.y = CuboidSegment(self.y.start, self.y.end)
        c.z = CuboidSegment(self.z.start, self.z.end)
        return c

    def print(self):
        print('x:', self.x.to_string(), 'y:', self.y.to_string(), 'z:', self.z.to_string(), 'on:', self.is_on())

    def is_on(self):
        return self.on == 'on'

    def is_in_valid_range(self, min_value, max_value):
        return self.x.is_in_valid_range(min_value, max_value) and self.y.is_in_valid_range(min_value, max_value) and self.z.is_in_valid_range(min_value, max_value)

    def num_cubes(self):
        return self.x.length() * self.y.length() * self.z.length()

    def add(self, another):
        return self.split(another)

    def is_overlapped(self, another):
        return self.x.is_overlapped(another.x) and self.y.is_overlapped(another.y) and self.z.is_overlapped(another.z)

    def split(self, another):
        splitteds = []
        cuboid = another.clone()

        while cuboid != None:
            if self.is_overlapped(cuboid):
                # Cut the bottom
                if cuboid.z.start < self.z.start:
                    c = Cuboid()
                    c.init_with_coordinates([cuboid.x.start, cuboid.x.end, cuboid.y.start, cuboid.y.end, cuboid.z.start, self.z.start - 1])
                    splitteds.append(c)
                    cuboid.z.start = self.z.start
                # Cut the top
                elif cuboid.z.end > self.z.end:
                    c = Cuboid()
                    c.init_with_coordinates([cuboid.x.start, cuboid.x.end, cuboid.y.start, cuboid.y.end, self.z.end + 1, cuboid.z.end])
                    splitteds.append(c)
                    cuboid.z.end = self.z.end
                # Cut the left
                elif cuboid.x.start < self.x.start:
                    c = Cuboid()
                    c.init_with_coordinates([cuboid.x.start, self.x.start - 1, cuboid.y.start, cuboid.y.end, cuboid.z.start, cuboid.z.end])
                    splitteds.append(c)
                    cuboid.x.start = self.x.start
                # Cut the right
                elif cuboid.x.end > self.x.end:
                    c = Cuboid()
                    c.init_with_coordinates([self.x.end + 1, cuboid.x.end, cuboid.y.start, cuboid.y.end, cuboid.z.start, cuboid.z.end])
                    splitteds.append(c)
                    cuboid.x.end = self.x.end
                # Cut the front
                elif cuboid.y.start < self.y.start:
                    c = Cuboid()
                    c.init_with_coordinates([cuboid.x.start, cuboid.x.end, cuboid.y.start, self.y.start - 1, cuboid.z.start, cuboid.z.end])
                    splitteds.append(c)
                    cuboid.y.start = self.y.start
                # Cut the back
                elif cuboid.y.end > self.y.end:
                    c = Cuboid()
                    c.init_with_coordinates([cuboid.x.start, cuboid.x.end, self.y.end + 1, cuboid.y.end, cuboid.z.start, cuboid.z.end])
                    splitteds.append(c)
                    cuboid.y.end = self.y.end
                else:
                    cuboid = None
            else:
                break
                        
        return splitteds

    def subtract(self, another):
        return self.split(another)
        

def split_data(row):
    row = row.iloc[0]
    row = row.split('=')[1]
    start, end = row.split('..')
    return (int(start), int(end))

def read_data(file_name):
    df = pd.read_csv(file_name, header=None, sep=' ')
    df[['x','y','z']] = df[1].str.split(',', expand=True)
    df.drop([1], axis=1, inplace=True)
    df['x'] = df[['x']].apply(split_data, axis=1)
    df['y'] = df[['y']].apply(split_data, axis=1)
    df['z'] = df[['z']].apply(split_data, axis=1)

    commands = []

    for i in range(len(df)):
        c = Cuboid()
        c.init(df.iloc[i, :])
        commands.append(c)
        c.print()

    return commands

def merge_cuboids(cuboids, cuboid):
    if cuboid.is_in_valid_range(-50, 50) == False:
        return cuboids
    if cuboid.is_on():
        return add_cuboids(cuboids, cuboid)
    else:
        return subtract_cuboids(cuboids, cuboid)

def add_cuboids(cuboids, cuboid):
    length = len(cuboids)
    if length > 0:
        splittings = [cuboid]
        is_splitted = False
        i = 0
        le = len(splittings)
        while i < le:
            index = 0
            while index < length:
                if cuboids[index].is_overlapped(splittings[i]):
                    splitteds = cuboids[index].add(splittings[i])
                    is_splitted = True
                    splittings.pop(i)

                    if len(splitteds) > 0:
                        for c in splitteds:
                            splittings.insert(i, c)
                    else:
                        index = 0

                    le = len(splittings)

                    if i >= le:
                        break
                else:
                    index += 1
            i += 1

        if is_splitted == True:
            cuboids.extend(splittings)
        else:
            cuboids.append(cuboid)
    else:
        cuboids.append(cuboid)

    return cuboids

def subtract_cuboids(cuboids, cuboid):
    length = len(cuboids)
    if length > 0:
        index = 0
        while index < length:
            if cuboid.is_overlapped(cuboids[index]):
                splitteds = cuboid.subtract(cuboids[index])
                cuboids.pop(index)

                if len(splitteds) > 0:
                    for c in splitteds:
                        cuboids.insert(index, c)
                    index += len(splitteds)

                length = len(cuboids)
            else:
                index += 1
    return cuboids

def check_overlaps(cuboids):
    for i in range(len(cuboids)):
        for j in range(len(cuboids) - 1):
            if i != j and cuboids[j].is_overlapped(cuboids[i]):
                print('overlapped:')
                cuboids[i].print()
                cuboids[j].print()

def count_cubes(cuboids, should_print):
    count = 0
    for i in range(len(cuboids)):
        count += cuboids[i].num_cubes()
        if should_print:
            cuboids[i].print()
            print(cuboids[i].num_cubes())
    return count

def main():
    cuboids = []
    commands = read_data('input2.txt')
    for command in commands:
        cuboids = merge_cuboids(cuboids, command)

    print('Num cuboids:',len(cuboids))
    count = count_cubes(cuboids, False)
    print('Num cubes:',count)



if __name__ == '__main__':
    main()
