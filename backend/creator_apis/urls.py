from . import views
from django.urls import path

urlpatterns = [
    path('group/', views.CreateGroup.as_view()),
    path('toggle_application/', views.ToggleApplication.as_view()),
    path('set_managing/<int:group_id>/', views.SetCurrentlyManagingGroup.as_view()),
    path('apply_for_admin/', views.ApplyForAdmin.as_view()),
    path('view_applications/', views.ViewApplications.as_view()),
    path('view_group_open_for_apply/', views.ViewGroupsOpenForApplication.as_view()),
    path('view_group_detail/<int:group_id>/', views.ViewGroupDetailPublic.as_view()),
    path('search_group/', views.SearchGroups.as_view()),
    path('view_user/<int:user_id>/', views.ViewMyProfilePublic.as_view()),
    path('view_myself/', views.ViewMyProfilePrivate.as_view()),
    path('view_my_sub_admins/', views.ViewAllSubAdmins.as_view()),
    path('set_new_sub_admin_email/', views.SetMessageForNewlyAcceptedApplicant.as_view()),
    path('set_new_subcriber_email/', views.SetMessageForNewSubscribers.as_view()),
    path('view_my_created_groups/', views.ViewMyCreatedGroups.as_view()),
    path('view_my_managed_groups/', views.ViewMyManagedGroups.as_view()),
    path('expel_sub_admin/<int:admin_id>/', views.ExpelSubAdmin.as_view()),
    path('view_all_my_posts/', views.ViewAllMyPosts.as_view()),
    path('view_all_pending_posts_for_group/', views.ViewPostsPendingApproval.as_view()),
    path('approve_post/<int:post_id>/', views.ApprovePost.as_view()),
    path('send_newsletter/<int:group_id>/', views.SendNewsletter.as_view()),
    path('subscribe/', views.SubscribeToGroup.as_view()),
    path('has_managing/', views.UserHasCurrentlyManaging.as_view()),

    
]