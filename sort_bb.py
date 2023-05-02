import numpy as np
import cv2
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster



def sort_bounding_boxes(bounding_boxes, threshold=20):
    # Tính toán khoảng cách giữa các bounding box dựa trên tọa độ y
    dist = pdist(np.array([[b[1], b[3]] for b in bounding_boxes]))
    
    # Sử dụng thuật toán hierarchical clustering để gom nhóm các bounding box lại với nhau
    linkage_matrix = linkage(dist, 'single')
    clusters = fcluster(linkage_matrix, threshold, criterion='distance')
    
    # Tạo danh sách các nhóm bounding box
    groups = {}
    for i, c in enumerate(clusters):
        if c not in groups:
            groups[c] = []
        groups[c].append(bounding_boxes[i])
    
    # Sắp xếp các bounding box trong mỗi nhóm theo thứ tự từ trái sang phải
    for group in groups.values():
        group.sort(key=lambda b: b[0])
    
    # Sắp xếp các nhóm theo thứ tự từ trên xuống dưới của ảnh
    groups = sorted(groups.values(), key=lambda g: g[0][1])
    
    return groups

if __name__ == "__main__":
    bounding_boxes = [[21, 109, 145, 229], [310, 68, 611, 191], [320, 209, 475, 245], [489, 197, 629, 236], [107, 11, 142, 31], [74, 10, 106, 30], [244, 114, 291, 145], [132, 34, 172, 49], [68, 35, 131, 49]]
    group = sort_bounding_boxes(bounding_boxes, threshold=20)

    list_bb = []
    for gr in group:
        list_bb += gr

    print(list_bb)

    # image = cv2.imread("test-case.jpg")
    # for id, box in enumerate(list_bb):
    #     x1, y1, x2, y2 = box
    #     cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #     cv2.putText(image, str(id), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # cv2.imwrite("visualize.jpg", image)