<h1> 재고관리 사이트</h1>

<hr>

<h4> 1) user requirements</h4>

<img src="image/user_interface.png" alt="img">

<br>

<h4> 2) path list</h4>
/ [name='item_list']<br>
detail/<int:pk> : [name='item_detail']<br>
create/ [name='item_create']<br>
update/<int:pk> [name='item_update']<br>
delete/<int:pk> [name='item_delete']<br>
plus/<int:pk> [name='item_plus']<br>
minus/<int:pk> [name='item_minus']<br><br>

company/ [name='company_list']<br>
company/detail/<int:pk> [name='company_detail']<br>
company/create/ [name='company_create']<br>
company/update/<int:pk> [name='company_update']<br>
company/delete/<int:pk> [name='company_delete']<br>