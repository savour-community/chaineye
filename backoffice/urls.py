from typing import Any, List
from django.contrib import admin
from django.urls import include, path
from backoffice.views.index import back_index
from backoffice.views.user import (
    back_user_list,
    backend_login,
    backend_logout
)
from backoffice.views.index import (
    back_index,
    back_blog_check,
    back_chainsafe,
    back_chainsafe_check
)

from backoffice.views.course import (
    back_course_list,
    back_course_check,
    back_course_artcle,
    back_course_comment
)


urlpatterns: List[Any] = [
    path(r'backend_login', backend_login, name='backend_login'),
    path(r'backend_logout', backend_logout, name='backend_logout'),
    path(r'back_user_list', back_user_list, name='back_user_list'),

    path(r'back_index', back_index, name='back_index'),
    path(r'<int:bid>/back_blog_check', back_blog_check, name='back_blog_check'),
    path(r'back_chainsafe', back_chainsafe, name='back_chainsafe'),
    path(r'<int:id>/back_chainsafe_check', back_chainsafe_check, name='back_chainsafe_check'),

    path(r'back_course_list', back_course_list, name='back_course_list'),
    path(r'<int:cid>/back_course_check', back_course_check, name='back_course_check'),
    path(r'<int:cid>/back_course_artcle', back_course_artcle, name='back_course_artcle'),
    path(r'<int:aid>/back_course_comment', back_course_comment, name='back_course_comment'),
]