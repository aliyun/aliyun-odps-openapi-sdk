// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

public class ListProjectsResponse extends TeaModel {
    @NameInMap("projects")
    @Validation(required = true)
    public java.util.List<Project> projects;

    @NameInMap("nextPageToken")
    public String nextPageToken;

    public static ListProjectsResponse build(java.util.Map<String, ?> map) throws Exception {
        ListProjectsResponse self = new ListProjectsResponse();
        return TeaModel.build(map, self);
    }

    public ListProjectsResponse setProjects(java.util.List<Project> projects) {
        this.projects = projects;
        return this;
    }
    public java.util.List<Project> getProjects() {
        return this.projects;
    }

    public ListProjectsResponse setNextPageToken(String nextPageToken) {
        this.nextPageToken = nextPageToken;
        return this;
    }
    public String getNextPageToken() {
        return this.nextPageToken;
    }

}
