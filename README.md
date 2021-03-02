DỰ ÁN BACKEND XÂY DỰNG WEB TIN TỨC VỚI DJANGO
---
MỤC TIÊU
---
  - Tìm hiểu django framework
  - Tìm hiểu kết nối dự án Django của mình với cơ sở dữ liệu
  - Xây dựng cơ bản hoàn thiện trang blogs tin tức
  - Tìm hiểu cách kiểm thử dự án django và cách viết test case
  - Nghiên cứu vấn đề bảo mật website

----------------------------------------------------------------
CẤU HÌNH 
  - Python (3.5, 3.6, 3.7, 3.8, 3.9)
  - [Start Bootstrap - Clean Blog](https://startbootstrap.com/theme/clean-blog/)
  - Django (2.2, 3.0, 3.1,3.1.2)
  - Khuyến khích và chỉ hỗ trợ chính thức bản phát hành bản vá mới nhất của từng dòng Python và Django.
  - 
  - 
----------------------------------------------------------------

Sử dụng khung công tác REST để xây dựng một API dựa trên mô hình đơn giản để truy cập người dùng và nhóm.

Khởi động một dự án mới
```
pip install django
pip install djangorestframework
django-admin startproject example .
./manage.py migrate
./manage.py createsuperuser
```
Bây giờ hãy chỉnh sửa blogs/admin.py mô-đun trong dự án:
```
from django.contrib import admin
from .models import theloai, baiviet
# Register your models here.

class sapxeptheloai(admin.ModelAdmin):
    list_display = ['tentheloai']
admin.site.register(theloai,sapxeptheloai)

class chinhbaiviet(admin.ModelAdmin):
    list_display = ['tenbaiviet', 'ngay']
    list_filter = ['ngay']
    search_fields = ['tenbaiviet']
admin.site.register(baiviet, chinhbaiviet)
```

----------------------------------------------------------------
<img   src="https://github.com/Phung82/WebNews/blob/master/img/001-home.PNG" width="900" height="500"/>
<p>Hình 1 Giao diện trang chủ</p>

<img   src="https://github.com/Phung82/WebNews/blob/master/img/001-Ngua.PNG" width="900" height="600"/>
<p>Hình 3 Một bài viết </p>

<img   src="https://github.com/Phung82/WebNews/blob/master/img/001-Lienlac.PNG" width="900" height="600"/>
<p>Hình 3 Giao diện trang liên lạc</p>

<img   src="https://github.com/Phung82/WebNews/blob/master/img/001-theloai.PNG" width="900" height="600"/>
<p>Hình 3 Giao diện trang quản trị - THỂ LOẠI</p>

<img   src="https://github.com/Phung82/WebNews/blob/master/img/001-BaiViet.PNG" width="900" height="500"/>
<p>Hình 3 Giao diện trang quản trị - BÀI VIẾTI</p>

---------------------------------------------------------------
Tài liệu & Hỗ trợ
-------

```
Tài liệu đầy đủ cho dự án có tại https://www.django-rest-framework.org/ .

Đối với các câu hỏi và hỗ trợ, hãy sử dụng nhóm thảo luận khung REST hoặc #restframeworktrên freenode IRC.
```
