import matplotlib.pyplot as plt
from matplotlib import patches

def draw_pitch(pitch_color="#FFFFFF", line_color="#000000", area="full"):
    
    """Plots a Football Pitch with dimensions 104X68
    Parameters:
    
    pitch_color (str):The color of the pitch. Default value is white.
    line_color (str):The color of the lines on the pitch. Default value is black.
    area (str):A vairable to decide whether we want half a pitch or full. Default value is full.
    """
    
    if area=='full':
        
        fig = plt.figure(figsize=(10.4,6.8))
        ax = fig.add_subplot(1,1,1)
        ax.patch.set_facecolor(pitch_color)
        ax.axis('off')
        
        #Outer Pitchlines
        outer_x = [0,104,104,0,0]
        outer_y = [0,0,68,68,0]
        plt.plot(outer_x,outer_y,color=line_color,zorder=5)
        
        #Centre line
        plt.plot([52,52],[0,68],color=line_color,zorder=5)
        
        #Outer Boxes
        left_outer_x = [104,87.5,87.5,104]
        left_outer_y = [13.84,13.84,54.16,54.16] 
        plt.plot(left_outer_x,left_outer_y,color=line_color,zorder=5)
        
        right_outer_x = [0,16.5,16.5,0]
        right_outer_y = [13.84,13.84,54.16,54.16] 
        plt.plot(right_outer_x,right_outer_y,color=line_color,zorder=5)
        
        #Goals
        left_goal_y = [30.34,30.34,37.66,37.66]
        left_goal_x = [0,-0.2,-0.2,0]
        plt.plot(left_goal_x,left_goal_y,color=line_color,zorder=5)
        
        right_goal_x = [104,104.2,104.2,104]
        right_goal_y = [30.34,30.34,37.66,37.66]
        plt.plot(right_goal_x,right_goal_y,color=line_color,zorder=5)
        
        #6 Yard Boxes
        left_six_x = [0,4.5,4.5,0]
        left_six_y = [24.84,24.84,43.16,43.16]
        plt.plot(left_six_x,left_six_y,color=line_color,zorder=5)
        
        right_six_x = [104,99.5,99.5,104]
        right_six_y = [24.84,24.84,43.16,43.16]
        plt.plot(right_six_x,right_six_y,color=line_color,zorder=5)
        
        #Penalty and centre spot
        plt.scatter(93,34,color=line_color,zorder=5)
        plt.scatter(11,34,color=line_color,zorder=5)
        plt.scatter(52,34,color=line_color,zorder=5)
        
        centre_circle = plt.Circle((52, 34), 9.15,ls='solid',lw=1.5,color=line_color, fill=False, zorder=2,alpha=1)
        left_circle = plt.Circle((10.5,34), 9.15,ls='solid',lw=1.5,color=line_color, fill=False, zorder=1,alpha=1)
        right_circle = plt.Circle((93.5,34), 9.15,ls='solid',lw=1.5,color=line_color, fill=False, zorder=1,alpha=1)

        #To hide the circle's extra part to only leave the D.
        rec1 = plt.Rectangle((87.5,20), 16,30,ls='-',color=pitch_color, zorder=1,alpha=1)
        rec2 = plt.Rectangle((0, 20), 16.5,30,ls='-',color=pitch_color, zorder=1,alpha=1)
        
        ax.add_patch(centre_circle)
        ax.add_patch(left_circle)
        ax.add_patch(right_circle)
        
        ax.add_patch(rec1)
        ax.add_patch(rec2)
        
    if area=="half":
        
        fig = plt.figure(figsize=(6.8,5.2))
        ax = fig.add_subplot(1,1,1)
        ax.patch.set_facecolor(pitch_color)
        ax.axis('off')
        
        #Outer Pitchlines
        outer_x = [0,0,68,68,0]
        outer_y = [0,52,52,0,0]
        plt.plot(outer_x,outer_y,color=line_color,zorder=5)
        
        #OuterBox
        box_x = [13.84,13.84,54.16,54.16]
        box_y = [52,35.5,35.5,52]
        plt.plot(box_x,box_y,color=line_color,zorder=5)
        
        #Goal
        goal_x = [30.34,30.34,37.66,37.66]
        goal_y = [52,52.2,52.2,52]
        plt.plot(goal_x,goal_y,color=line_color,zorder=5)
        
        #6 Yard Box
        six_x = [24.84,24.84,43.16,43.16]
        six_y = [52,47.5,47.5,52]
        plt.plot(six_x,six_y,color=line_color,zorder=5)
        
        #Centre Sport and Penalty Spot 
        plt.scatter(34,0,color=line_color,zorder=5)
        plt.scatter(34,41,color=line_color,zorder=5)
        
        #Centre circle and D
        centre_circle = plt.Circle((34, 0), 9.15,ls='solid',lw=1.5,color=line_color, fill=False, zorder=2,alpha=1)
        upper_circle = plt.Circle((34,41.5), 9.15,ls='solid',lw=1.5,color=line_color, fill=False, zorder=1,alpha=1)
        
        #Rectangle to hide the extra part of the D
        rec1 = plt.Rectangle((23, 35.5), 30,16.5,ls='-',color=_color, zorder=1,alpha=1)
        
        
        ax.add_patch(centre_circle)
        ax.add_patch(upper_circle)
        ax.add_patch(rec1)
