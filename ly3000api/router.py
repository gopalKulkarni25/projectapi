from projectapi.viewsets import ProjectViewset

from issueapi.viewsets import IssueViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('project', ProjectViewset)
router.register('issue', IssueViewset)

