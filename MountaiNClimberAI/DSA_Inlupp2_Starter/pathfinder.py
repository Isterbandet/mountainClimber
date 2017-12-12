import sys, math, random

class Pathfinder:
    def __init__(self, visualiser, map):
        self._visualiser = visualiser
        self._map = map


    def findCheapestPath(self):
        self.costlist =[]
        self.pathlist = []
        self.startingpos = 0
        self.costindex = 0


        # Mark's silly algorithm for finding the cheapest path:
        #   Use random logic - virtually gauranteed to give the correct answer
        #   eventually if we just run it enough times.
        #   NOTE: Since problem is NP-hard - we won't know for sure that it is
        #         the correct answer when we get it which is a bummer.

        # Starting at a random position on the left:
        while self.startingpos <= self._map.getHeight()- 1:
            #starting_row = random.randint( 0, self._map.getHeight() )

        # Search for one random path:
            ( cost, path ) = self.findPath(self.startingpos)
            self.startingpos += 1

        # It is the only path we have found, visualise it:
            self._visualiser.addPath(path)
            self.pathlist.append(path)
            self.costlist.append(cost)







        # The only path so it must also be the best path, visualise that:
            if self.startingpos > self._map.getHeight() - 1:

                cheapest= min(self.costlist)

                for i in range(0, len(self.costlist)):
                    if self.costlist[i] == cheapest:
                        self.costindex = i
                        break







                self._visualiser.setBestPath(self.pathlist[self.costindex])

        # And the cost of this so called "best" path:
                self._visualiser.setBestPathCost(self.costlist[self.costindex] )

        # What next?  Can you do better than random?
        # TODO:  Step 1 - a greeedy algorithm from a random starting position
        # TODO:  Step 2 - best greedy of all possible starting positions
        # TODO:  Step 3 - improve even more!
                return


    def findPath(self, starting_row  ):
        # Code to find one path from left to right through the map
        # And return the total "cost" and path
        # Current finds only a random path - can you make it better?

        matrix = self._map.getMatrix()
        rows = self._map.getHeight()
        cols = self._map.getWidth()


        row = starting_row

        cost = 0
        col=0
        path=[ row ]

        while col+1 < cols:
            # how high are we right now?
            current_altitude = matrix[row][col]

            straight = matrix[row][col + 1]
            gostraight = int(math.fabs(current_altitude - straight))

            if row  == self._map.getHeight()- 1:
                godown = sys.maxsize
            else:
                down = matrix[row + 1][col + 1]
                godown = int(math.fabs(current_altitude - down))

            if row  == 0:
                goupp = sys.maxsize
            else:
                upp = matrix[row - 1][col + 1]
                goupp = int(math.fabs(current_altitude - upp))





            # Pick a random direction - up/right,  right,  down/right
           # r = random.randint(-1,1)
            #row = row + r
            if goupp < gostraight and goupp < godown:

                    row =row -1
            if godown < gostraight and godown< goupp:

                    row = row+1
            if gostraight < goupp and gostraight< godown:
                row = row

            col += 1

            # how high are we now?
            new_altitude = matrix[row][col]

            # change in height:
            delta = int( math.fabs( new_altitude - current_altitude ) )

            # cost is the absolute change in height per step
            cost += delta

            # add this step to the path we are following
            path.append( row )


        return ( cost, path )

