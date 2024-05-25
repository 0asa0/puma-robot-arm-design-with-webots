import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_custom_3d_gps_data(file_path, skip_factor=1):
    with open(file_path, "r") as file:
        data = file.readlines()
        filtered_data = [line.split(",") for idx, line in enumerate(data) if idx % skip_factor == 0]
        x = [float(line[0]) for line in filtered_data]
        y = [float(line[1]) for line in filtered_data]
        z = [float(line[2]) for line in filtered_data]

        fig = plt.figure(figsize=(10, 8))  
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, c=range(len(x)), cmap='viridis', marker='o', alpha=0.5) 
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Robot Workspace Detection')
        plt.show()
        
# skip factor veri sadeleştirmek için.
plot_custom_3d_gps_data("gps_data.txt", skip_factor=1)  
# 3 boyutlu haritanın oluşturulması için bu python kodunun ayrıca çalıştırılması lazım.