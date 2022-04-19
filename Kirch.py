import cv2     # Thư viện OpenCV
import numpy as np   # Thư viện numy để làm việc dữ liệu kiểu mảng
import matplotlib.pyplot as plt # import thư viện matplotlib để vẽ ảnh

# Định nghĩa hàm Tich_chap() để lọc Trung bình, Trung bình có trọng số và lọc Gaussian
def Tich_chap(img,mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp   =  img[i-1, j-1]    * mask[0, 0]\
                   +  img[i, j-1]      * mask[0, 1]\
                   +  img[i+1, j - 1]  * mask[0, 2]\
                   +  img[i-1, j]      * mask[1, 0]\
                   +  img[i, j]        * mask[1, 1]\
                   +  img[i+1, j]      * mask[1, 2]\
                   +  img[i - 1, j+1]  * mask[2, 0]\
                   +  img[i, j + 1]    * mask[2, 1]\
                   +  img[i + 1, j + 1]* mask[2, 2]
            img_new[i, j]= temp
    img_new = img_new.astype(np.uint8)
    return img_new

# Định nghĩa Kirch theo hướng 0 độ 
loc_Kirch1 = np.array(([5, 5, -3],
                       [5, 0, -3],
                       [-3, -3, -3]), dtype="float")

loc_Kirch2 = np.array(([5, 5, 5],
                       [-3, 0, -3],
                       [-3, -3, -3]), dtype="float")

loc_Kirch3 = np.array(([-3, 5, 5],
                       [-3, 0, 5],
                       [-3, -3, -3]), dtype="float")

loc_Kirch4 = np.array(([-3, -3, 5],
                       [-3, 0, 5],
                       [-3, -3, 5]), dtype="float")

loc_Kirch5 = np.array(([-3, -3, -3],
                       [-3, 0, 5],
                       [-3, 5, 5]), dtype="float")

loc_Kirch6 = np.array(([-3, -3, -3],
                       [-3, 0, -3],
                       [5, 5, 5]), dtype="float")

loc_Kirch7 = np.array(([-3, -3, -3],
                       [5, 0, -3],
                       [5, 5, -3]), dtype="float")

loc_Kirch8 = np.array(([5, -3, -3],
                       [5, 0, -3],
                       [5, -3, -3]), dtype="float")

fig = plt.figure(figsize=(25, 16)) # Tạo vùng vẽ tỷ lệ 16:9
(ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9), (ax10, ax11, ax12) = fig.subplots(4, 3) 

# Đọc và hiển thị ảnh gốc
image = cv2.imread('opencv2/th.jpeg', 0)
ax1.imshow(image, cmap='gray')
ax1.set_title("Ảnh gốc")

# Lọc Kirch theo hướng 0 và hiển thị ảnh
img_Kirch1 = Tich_chap(image, loc_Kirch1) #Gọi hàm tích chập
ax2.imshow(img_Kirch1, cmap='gray')
ax2.set_title("Ảnh lọc Kirch 1")

# Lọc Kirch theo hướng 45 và hiển thị ảnh
img_Kirch2 = Tich_chap(image, loc_Kirch2) #Gọi hàm tích chập
ax3.imshow(img_Kirch2, cmap='gray')
ax3.set_title("Ảnh lọc Kirch 2")

# Lọc Kirch theo hướng 90 và hiển thị ảnh
img_Kirch3 = Tich_chap(image, loc_Kirch3) #Gọi hàm tích chập
ax4.imshow(img_Kirch3, cmap='gray')
ax4.set_title("Ảnh lọc Kirch 3")

# Lọc Kirch theo hướng 135 và hiển thị ảnh
img_Kirch4 = Tich_chap(image, loc_Kirch4) #Gọi hàm tích chập
ax5.imshow(img_Kirch4, cmap='gray')
ax5.set_title("Ảnh lọc Kirch 4")

# Lọc Kirch theo hướng 180 và hiển thị ảnh
img_Kirch5 = Tich_chap(image, loc_Kirch5) #Gọi hàm tích chập
ax6.imshow(img_Kirch5, cmap='gray')
ax6.set_title("Ảnh lọc Kirch 5")

# Lọc Kirch theo hướng 225 và hiển thị ảnh
img_Kirch6 = Tich_chap(image, loc_Kirch6) #Gọi hàm tích chập
ax7.imshow(img_Kirch6, cmap='gray')
ax7.set_title("Ảnh lọc Kirch 6")

# Lọc Kirch theo hướng 270 và hiển thị ảnh
img_Kirch7 = Tich_chap(image, loc_Kirch7) #Gọi hàm tích chập
ax8.imshow(img_Kirch7, cmap='gray')
ax8.set_title("Ảnh lọc Kirch 7")

# Lọc Kirch theo hướng 315 và hiển thị ảnh
img_Kirch8 = Tich_chap(image, loc_Kirch8) #Gọi hàm tích chập
ax9.imshow(img_Kirch8, cmap='gray')
ax9.set_title("Ảnh lọc Kirch 8")


# Ảnh tổng Kirch theo 8 hướng và hiển thị ảnh
img_Kirch12345678 = img_Kirch1 + img_Kirch2 + img_Kirch3 + img_Kirch4 + img_Kirch5 + img_Kirch6 + img_Kirch7 + img_Kirch8
ax10.imshow(img_Kirch12345678, cmap='gray')
ax10.set_title("Ảnh lọc Kirch 1 +...+ Ảnh lọc Kirch 8")

# Ảnh cuối cùng = ảnh gốc + Ảnh tổng Kirch theo hướng 1 và Kirch
# theo hướng 2 và hiển thị ảnh
img_Kirch12345678_ketqua = image + img_Kirch12345678
ax11.imshow(img_Kirch12345678_ketqua, cmap='gray')
ax11.set_title("Ảnh Kết quả")



# Hiển thị vùng vẽ
plt.show()