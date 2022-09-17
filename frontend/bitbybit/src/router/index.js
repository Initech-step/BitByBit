import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignIn from '../views/SignInView.vue'
import SignUp from '../views/SignUpView.vue'
import Search from '../views/SearchView.vue'
import UserProfileView from '../views/UserProfileView.vue'
import CreateGroupView from '../views/CreateGroupView.vue'
import CurrentlyManagingView from '../views/CurrentlyManagingView.vue'
import MakePostView from '../views/MakePostView.vue'
import ManageGroupView from '../views/ManageGroupView.vue'
import GroupDetailView from '../views/GroupDetailView.vue'
import SubManageView from '../views/SubManageView.vue'

// used for accepting or declining applications
import ApplicationsView from '../views/ApplicationsView.vue'

// used for seeing groups open for application
import ApplicationsToGroupView from '../views/ApplyToGroupView.vue'

// application form used for applying to groups
import ApplicationFormView from '../views/ApplicationFormView.vue'

// set currently managing
import SetCurrentlyManagingView from '../views/SetCurrentlyManagingView.vue'

import viewPendingPostsView from '../views/viewPendingPosts.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignIn
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/search',
      name: 'search',
      component: Search
    },
    {
      path: '/admin_panel',
      name: 'admin_panel',
      component: UserProfileView
    },
    {
      path: '/admin_panel/create_group',
      name: 'create_group',
      component: CreateGroupView
    },
    {
      path: '/admin_panel/currently_managing',
      name: 'currently_managing',
      component: CurrentlyManagingView
    },
    {
      path: '/admin_panel/group/make_post/:g_id',
      name: 'make_post',
      component: MakePostView
    },
    {
      path: '/admin_panel/group/manage_group',
      name: 'manage_group',
      component: ManageGroupView
    },
    {
      path: '/group_details/:g_id',
      name: 'group_details',
      component: GroupDetailView
    },
    {
      path: '/group/sub_manage',
      name: 'sub_manage',
      component: SubManageView
    },
    {
      path: '/application/view_application',
      name: 'view_application',
      component: ApplicationsView
    },

    {
      path: '/application/groups_open',
      name: 'groups_open',
      component: ApplicationsToGroupView
    },

    {
      path: '/application/apply_to_group/:g_id',
      name: 'apply_to_group',
      component: ApplicationFormView
    },

    {
      path: '/set_managing',
      name: 'set_managing',
      component: SetCurrentlyManagingView
    },
    {
      path: '/view_pending_posts',
      name: 'view_pending_posts',
      component: viewPendingPostsView
    },
    
  ]
})

export default router
