from django.urls import include, path

from video_streaming.apis import (
    FileDirectUploadFinishApi,
    FileDirectUploadStartApi,
)


urlpatterns = [
    path(
        "upload/",
        include(
            (
                [
                    path(
                        "direct/",
                        include(
                            (
                                [
                                    path("start/", FileDirectUploadStartApi.as_view(), name="start"),
                                    path("finish/", FileDirectUploadFinishApi.as_view(), name="finish"),
                                ],
                                "direct",
                            )
                        ),
                    ),
                ],
                "upload",
            )
        ),
    )
]