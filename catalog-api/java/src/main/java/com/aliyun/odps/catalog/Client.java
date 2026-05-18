// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog;

import com.aliyun.tea.*;
import com.aliyun.odps.catalog.models.*;

public class Client extends com.aliyun.odps.Client {

    public Client(com.aliyun.odps.models.Config config) throws Exception {
        super(config);
    }


    // 限流：每用户每秒最多 10 次请求
    public Table updateTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(table, "PUT", this.getTablePath(table), null, runtime), new Table());
    }

    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deleteTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithoutModel(table, "DELETE", this.getTablePath(table), null, runtime), new HttpResponse());
    }

    // 限流：每用户每秒最多 10 次请求
    public Table createTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(table, "POST", this.getTablesPath(table), null, runtime), new Table());
    }

    // 限流：每用户每秒最多 100 次请求
    public Table getTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(table, "GET", this.getTablePath(table), null, runtime), new Table());
    }

    // 限流：每用户每秒最多 10 次请求
    public ListTablesResponse listTables(String projectId, String schemaName, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/tables";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListTablesResponse(), "GET", path, query, runtime), new ListTablesResponse());
    }

    // 限流：每用户每秒最多 10 次请求
    public Policy setTablePolicy(Table table, SetPolicyRequest policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getTablePath(table) + ":setPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    // 限流：每用户每秒最多 100 次请求
    public Policy getTablePolicy(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getTablePath(table) + ":getPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    public String getTablePath(Table table) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(table.schemaName)) {
            return "/api/catalog/v1alpha/projects/" + table.projectId + "/schemas/default/tables/" + table.tableName + "";
        } else {
            return "/api/catalog/v1alpha/projects/" + table.projectId + "/schemas/" + table.schemaName + "/tables/" + table.tableName + "";
        }

    }

    public String getTablesPath(Table table) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(table.schemaName)) {
            return "/api/catalog/v1alpha/projects/" + table.projectId + "/schemas/default/tables";
        } else {
            return "/api/catalog/v1alpha/projects/" + table.projectId + "/schemas/" + table.schemaName + "/tables";
        }

    }

    // 限流：每用户每秒最多 10 次请求
    public Connection createConnection(String namespace, Connection connection) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespace + "/connections";
        return TeaModel.toModel(this.requestWithModel(connection, "POST", path, null, runtime), new Connection());
    }

    // 限流：每用户每秒最多 10 次请求
    public ListConnectionsResponse listConnections(String namespace, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespace + "/connections";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListConnectionsResponse(), "GET", path, query, runtime), new ListConnectionsResponse());
    }

    // 限流：每用户每秒最多 100 次请求
    public Connection getConnection(String namespace, String connectionName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getConnectionPath(namespace, connectionName);
        return TeaModel.toModel(this.requestWithModel(new Connection(), "GET", path, null, runtime), new Connection());
    }

    // 限流：每用户每秒最多 10 次请求
    public Connection updateConnection(String namespace, String connectionName, Connection connection, String updateMask) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getConnectionPath(namespace, connectionName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("updateMask", updateMask);
        return TeaModel.toModel(this.requestWithModel(connection, "PATCH", path, query, runtime), new Connection());
    }

    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deleteConnection(String namespace, String connectionName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getConnectionPath(namespace, connectionName);
        return TeaModel.toModel(this.requestWithoutModel(new Connection(), "DELETE", path, null, runtime), new HttpResponse());
    }

    // 限流：每用户每秒最多 10 次请求
    public Policy setConnectionPolicy(String namespace, String connectionName, SetPolicyRequest request) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getConnectionPath(namespace, connectionName) + ":setPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(request, "POST", path, query, runtime), new Policy());
    }

    // 限流：每用户每秒最多 100 次请求
    public Policy getConnectionPolicy(String namespace, String connectionName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getConnectionPath(namespace, connectionName) + ":getPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    public String getConnectionPath(String namespace, String connectionName) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/connections/" + connectionName + "";
    }

    // Path generation helper
    public String getRolePath(String namespace, String roleName) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/roles/" + roleName + "";
    }

    // Create role
    // 限流：每用户每秒最多 10 次请求
    public Role createRole(String namespace, Role role) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespace + "/roles";
        return TeaModel.toModel(this.requestWithModel(role, "POST", path, null, runtime), new Role());
    }

    // Delete role
    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deleteRole(String namespace, String roleName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getRolePath(namespace, roleName);
        return TeaModel.toModel(this.requestWithoutModel(new Role(), "DELETE", path, null, runtime), new HttpResponse());
    }

    // Get role
    // 限流：每用户每秒最多 100 次请求
    public Role getRole(String namespace, String roleName, String view) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getRolePath(namespace, roleName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(view)) {
            query.put("view", view);
        }

        return TeaModel.toModel(this.requestWithModel(new Role(), "GET", path, query, runtime), new Role());
    }

    // List roles
    // 限流：每用户每秒最多 10 次请求
    public ListRolesResponse listRoles(String namespace, Integer pageSize, String pageToken, String view, Boolean showDeleted) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespace + "/roles";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        if (!com.aliyun.teautil.Common.isUnset(view)) {
            query.put("view", view);
        }

        if (!com.aliyun.teautil.Common.isUnset(showDeleted)) {
            query.put("showDeleted", com.aliyun.odps.utils.TeaUtils.toString(showDeleted));
        }

        return TeaModel.toModel(this.requestWithModel(new ListRolesResponse(), "GET", path, query, runtime), new ListRolesResponse());
    }

    // Update role
    // 限流：每用户每秒最多 10 次请求
    public Role updateRole(String namespace, String roleName, Role role, String updateMask) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getRolePath(namespace, roleName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(updateMask)) {
            query.put("updateMask", updateMask);
        }

        return TeaModel.toModel(this.requestWithModel(role, "PATCH", path, query, runtime), new Role());
    }

    // Set role policy
    // 限流：每用户每秒最多 10 次请求
    public Policy setRolePolicy(String namespace, String roleName, SetPolicyRequest policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getRolePath(namespace, roleName) + ":setPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    // Get role policy
    // 限流：每用户每秒最多 100 次请求
    public Policy getRolePolicy(String namespace, String roleName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getRolePath(namespace, roleName) + ":getPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    // Path generation helpers
    public String getTaxonomyPath(String namespace, String taxonomyId) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/taxonomies/" + taxonomyId + "";
    }

    public String getPolicyTagPath(String namespace, String taxonomyId, String policyTagId) throws Exception {
        return "" + this.getTaxonomyPath(namespace, taxonomyId) + "/policyTags/" + policyTagId + "";
    }

    // Taxonomy operations
    // 限流：每用户每秒最多 10 次请求
    public Taxonomy createTaxonomy(String namespace, Taxonomy taxonomy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespace + "/taxonomies";
        return TeaModel.toModel(this.requestWithModel(taxonomy, "POST", path, null, runtime), new Taxonomy());
    }

    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deleteTaxonomy(String namespace, String taxonomyId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTaxonomyPath(namespace, taxonomyId);
        return TeaModel.toModel(this.requestWithoutModel(new Taxonomy(), "DELETE", path, null, runtime), new HttpResponse());
    }

    // 限流：每用户每秒最多 100 次请求
    public Taxonomy getTaxonomy(String namespace, String taxonomyId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTaxonomyPath(namespace, taxonomyId);
        return TeaModel.toModel(this.requestWithModel(new Taxonomy(), "GET", path, null, runtime), new Taxonomy());
    }

    // 限流：每用户每秒最多 10 次请求
    public ListTaxonomiesResponse listTaxonomies(String namespace, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespace + "/taxonomies";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListTaxonomiesResponse(), "GET", path, query, runtime), new ListTaxonomiesResponse());
    }

    // 限流：每用户每秒最多 10 次请求
    public Taxonomy updateTaxonomy(String namespace, String taxonomyId, Taxonomy taxonomy, String updateMask) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTaxonomyPath(namespace, taxonomyId);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(updateMask)) {
            query.put("updateMask", updateMask);
        }

        return TeaModel.toModel(this.requestWithModel(taxonomy, "PATCH", path, query, runtime), new Taxonomy());
    }

    // 限流：每用户每秒最多 10 次请求
    public Policy setTaxonomyPolicy(String namespace, String taxonomyId, SetPolicyRequest policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getTaxonomyPath(namespace, taxonomyId) + ":setPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "setPolicy");
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    // 限流：每用户每秒最多 100 次请求
    public Policy getTaxonomyPolicy(String namespace, String taxonomyId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getTaxonomyPath(namespace, taxonomyId) + ":getPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    // PolicyTag operations
    // 限流：每用户每秒最多 10 次请求
    public PolicyTag createPolicyTag(String namespace, String taxonomyId, PolicyTag policyTag) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getTaxonomyPath(namespace, taxonomyId) + "/policyTags";
        return TeaModel.toModel(this.requestWithModel(policyTag, "POST", path, null, runtime), new PolicyTag());
    }

    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deletePolicyTag(String namespace, String taxonomyId, String policyTagId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getPolicyTagPath(namespace, taxonomyId, policyTagId);
        return TeaModel.toModel(this.requestWithoutModel(new PolicyTag(), "DELETE", path, null, runtime), new HttpResponse());
    }

    // 限流：每用户每秒最多 100 次请求
    public PolicyTag getPolicyTag(String namespace, String taxonomyId, String policyTagId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getPolicyTagPath(namespace, taxonomyId, policyTagId);
        return TeaModel.toModel(this.requestWithModel(new PolicyTag(), "GET", path, null, runtime), new PolicyTag());
    }

    // 限流：每用户每秒最多 10 次请求
    public ListPolicyTagsResponse listPolicyTags(String namespace, String taxonomyId, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getTaxonomyPath(namespace, taxonomyId) + "/policyTags";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListPolicyTagsResponse(), "GET", path, query, runtime), new ListPolicyTagsResponse());
    }

    // 限流：每用户每秒最多 10 次请求
    public PolicyTag updatePolicyTag(String namespace, String taxonomyId, String policyTagId, PolicyTag policyTag, String updateMask) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getPolicyTagPath(namespace, taxonomyId, policyTagId);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(updateMask)) {
            query.put("updateMask", updateMask);
        }

        return TeaModel.toModel(this.requestWithModel(policyTag, "PATCH", path, query, runtime), new PolicyTag());
    }

    // 限流：每用户每秒最多 10 次请求
    public Policy setPolicyTagPolicy(String namespace, String taxonomyId, String policyTagId, SetPolicyRequest policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getPolicyTagPath(namespace, taxonomyId, policyTagId) + ":setPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    // 限流：每用户每秒最多 100 次请求
    public Policy getPolicyTagPolicy(String namespace, String taxonomyId, String policyTagId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getPolicyTagPath(namespace, taxonomyId, policyTagId) + ":getPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    // 限流：每用户每秒最多 10 次请求
    public DataPolicy createDataPolicy(String namespace, DataPolicy dataPolicy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataPoliciesPath(namespace);
        return TeaModel.toModel(this.requestWithModel(dataPolicy, "POST", path, null, runtime), new DataPolicy());
    }

    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deleteDataPolicy(String namespace, String dataPolicyName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataPolicyPath(namespace, dataPolicyName);
        return TeaModel.toModel(this.requestWithoutModel(new DataPolicy(), "DELETE", path, null, runtime), new HttpResponse());
    }

    // 限流：每用户每秒最多 100 次请求
    public DataPolicy getDataPolicy(String namespace, String dataPolicyName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataPolicyPath(namespace, dataPolicyName);
        return TeaModel.toModel(this.requestWithModel(new DataPolicy(), "GET", path, null, runtime), new DataPolicy());
    }

    // 限流：每用户每秒最多 10 次请求
    public ListDataPoliciesResponse listDataPolicies(String namespace, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataPoliciesPath(namespace);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListDataPoliciesResponse(), "GET", path, query, runtime), new ListDataPoliciesResponse());
    }

    // 限流：每用户每秒最多 10 次请求
    public Policy setDataPolicyPolicy(String namespace, String dataPolicyName, SetPolicyRequest request) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getDataPolicyPath(namespace, dataPolicyName) + ":setPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(request, "POST", path, query, runtime), new Policy());
    }

    // 限流：每用户每秒最多 100 次请求
    public Policy getDataPolicyPolicy(String namespace, String dataPolicyName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getDataPolicyPath(namespace, dataPolicyName) + ":getPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    public String getDataPolicyPath(String namespace, String dataPolicyName) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/dataPolicies/" + dataPolicyName + "";
    }

    public String getDataPoliciesPath(String namespace) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/dataPolicies";
    }

    // Paths
    public String getProjectPath(String projectId) throws Exception {
        return "/api/catalog/v1alpha/projects/" + projectId + "";
    }

    public String getSchemaPath(String projectId, String schemaName) throws Exception {
        return "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "";
    }

    // Methods
    // 限流：每用户每秒最多 10 次请求
    public ListProjectsResponse listProjects(Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListProjectsResponse(), "GET", "/api/catalog/v1alpha/projects", query, runtime), new ListProjectsResponse());
    }

    // 限流：每用户每秒最多 100 次请求
    public Project getProject(String projectId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(new Project(), "GET", this.getProjectPath(projectId), null, runtime), new Project());
    }

    // 限流：每用户每秒最多 10 次请求
    public Schema createSchema(String projectId, Schema schema) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/projects/" + projectId + "/schemas";
        return TeaModel.toModel(this.requestWithModel(schema, "POST", path, null, runtime), new Schema());
    }

    // 限流：每用户每秒最多 10 次请求
    public ListSchemasResponse listSchemas(String projectId, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/projects/" + projectId + "/schemas";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListSchemasResponse(), "GET", path, query, runtime), new ListSchemasResponse());
    }

    // 限流：每用户每秒最多 100 次请求
    public Schema getSchema(String projectId, String schemaName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(new Schema(), "GET", this.getSchemaPath(projectId, schemaName), null, runtime), new Schema());
    }

    // 限流：每用户每秒最多 10 次请求
    public Schema updateSchema(String projectId, String schemaName, String updateMask, Schema schema) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getSchemaPath(projectId, schemaName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("updateMask", updateMask);
        return TeaModel.toModel(this.requestWithModel(schema, "PATCH", path, query, runtime), new Schema());
    }

    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deleteSchema(String projectId, String schemaName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getSchemaPath(projectId, schemaName);
        return TeaModel.toModel(this.requestWithoutModel(new Schema(), "DELETE", path, null, runtime), new HttpResponse());
    }

    // 限流：每用户每秒最多 10 次请求
    public Policy setSchemaPolicy(String projectId, String schemaName, SetPolicyRequest policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getSchemaPath(projectId, schemaName) + ":setPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    // 限流：每用户每秒最多 100 次请求
    public Policy getSchemaPolicy(String projectId, String schemaName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getSchemaPath(projectId, schemaName) + ":getPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    // Path Functions
    public String getTablePartitionsPath(String projectId, String schemaName, String tableName) throws Exception {
        return "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/tables/" + tableName + "/partitions";
    }

    // Methods
    // 限流：每用户每秒最多 10 次请求
    public ListPartitionsResponse listPartitions(String projectId, String schemaName, String tableName, Integer pageSize, String pageToken, String query, String view) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTablePartitionsPath(projectId, schemaName, tableName);
        java.util.Map<String, String> params = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            params.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            params.put("pageToken", pageToken);
        }

        if (!com.aliyun.teautil.Common.isUnset(query)) {
            params.put("query", query);
        }

        if (!com.aliyun.teautil.Common.isUnset(view)) {
            params.put("view", view);
            if (com.aliyun.teautil.Common.equalString(view, "FULL")) {
                params.put("apiScope", "inner");
            }

        }

        return TeaModel.toModel(this.requestWithModel(new ListPartitionsResponse(), "GET", path, params, runtime), new ListPartitionsResponse());
    }

    public String getDataScanPath(String namespace, String dataScanName) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/dataScans/" + dataScanName + "";
    }

    public String getDataScansPath(String namespace) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/dataScans";
    }

    public String getTriggerDataScanPath(String namespace, String dataScanName) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/dataScans/" + dataScanName + ":trigger";
    }

    // 限流：每用户每秒最多 10 次请求
    public HttpResponse triggerDataScan(String namespace, String dataScanName) throws Exception {
        return TeaModel.toModel(this.requestWithoutModel(new ScanJob(), "POST", this.getTriggerDataScanPath(namespace, dataScanName), null, new com.aliyun.teautil.models.RuntimeOptions()), new HttpResponse());
    }

    // 限流：每用户每秒最多 10 次请求
    public DataScan updateDataScan(String namespace, DataScan dataScan, String updateMask) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("updateMask", updateMask);
        return TeaModel.toModel(this.requestWithModel(dataScan, "PATCH", this.getDataScanPath(namespace, dataScan.scanName), query, runtime), new DataScan());
    }

    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deleteDataScan(String namespace, String dataScanName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithoutModel(new DataScan(), "DELETE", this.getDataScanPath(namespace, dataScanName), null, runtime), new HttpResponse());
    }

    // 限流：每用户每秒最多 10 次请求
    public DataScan createDataScan(String namespace, DataScan dataScan) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(dataScan, "POST", this.getDataScansPath(namespace), null, runtime), new DataScan());
    }

    // 限流：每用户每秒最多 100 次请求
    public DataScan getDataScan(String namespace, String dataScanName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(new DataScan(), "GET", this.getDataScanPath(namespace, dataScanName), null, runtime), new DataScan());
    }

    // 限流：每用户每秒最多 10 次请求
    public ListDataScansResponse listDataScans(String namespace, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataScansPath(namespace);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListDataScansResponse(), "GET", path, query, runtime), new ListDataScansResponse());
    }

    public String getDataScanJobsPath(String namespace, String dataScanName) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/dataScans/" + dataScanName + "/scanJobs";
    }

    // 限流：每用户每秒最多 10 次请求
    public ListDataScanJobsResponse listDataScanJobs(String namespace, String dataScanName, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataScanJobsPath(namespace, dataScanName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListDataScanJobsResponse(), "GET", path, query, runtime), new ListDataScanJobsResponse());
    }

    // 路径生成函数
    public String getModelPath(String projectId, String schemaName, String modelName, String versionName) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(versionName)) {
            return "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/models/" + modelName + "";
        } else {
            return "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/models/" + modelName + "@" + versionName + "";
        }

    }

    // 创建模型
    // 限流：每用户每秒最多 10 次请求
    public Model createModel(String projectId, String schemaName, Model model) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/models";
        return TeaModel.toModel(this.requestWithModel(model, "POST", path, null, runtime), new Model());
    }

    // 列出模型
    // 限流：每用户每秒最多 10 次请求
    public ListModelsResponse listModels(String projectId, String schemaName, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/models";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListModelsResponse(), "GET", path, query, runtime), new ListModelsResponse());
    }

    // 获取模型
    // 限流：每用户每秒最多 100 次请求
    public Model getModel(String projectId, String schemaName, String modelName, String versionName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getModelPath(projectId, schemaName, modelName, versionName);
        return TeaModel.toModel(this.requestWithModel(new Model(), "GET", path, null, runtime), new Model());
    }

    // 更新模型
    // 限流：每用户每秒最多 10 次请求
    public Model updateModel(String projectId, String schemaName, String modelName, Model model, String updateMask, String versionName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getModelPath(projectId, schemaName, modelName, versionName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(updateMask)) {
            query.put("updateMask", updateMask);
        }

        return TeaModel.toModel(this.requestWithModel(model, "PATCH", path, query, runtime), new Model());
    }

    // 删除模型
    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deleteModel(String projectId, String schemaName, String modelName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getModelPath(projectId, schemaName, modelName, null);
        return TeaModel.toModel(this.requestWithoutModel(null, "DELETE", path, null, runtime), new HttpResponse());
    }

    // 创建模型版本
    // 限流：每用户每秒最多 10 次请求
    public Model createModelVersion(String projectId, String schemaName, String modelName, Model model) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/models/" + modelName + ":createVersion";
        return TeaModel.toModel(this.requestWithModel(model, "POST", path, null, runtime), new Model());
    }

    // 删除模型版本
    // 限流：每用户每秒最多 10 次请求
    public HttpResponse deleteModelVersion(String projectId, String schemaName, String modelName, String versionName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/models/" + modelName + "@" + versionName + ":deleteVersion";
        return TeaModel.toModel(this.requestWithoutModel(null, "DELETE", path, null, runtime), new HttpResponse());
    }

    // 列出模型版本
    // 限流：每用户每秒最多 10 次请求
    public ListModelVersionsResponse listModelVersions(String projectId, String schemaName, String modelName, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/models/" + modelName + ":listVersions";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListModelVersionsResponse(), "GET", path, query, runtime), new ListModelVersionsResponse());
    }

    // 获取模型策略
    // 限流：每用户每秒最多 100 次请求
    public Policy getModelPolicy(String projectId, String schemaName, String modelName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getModelPath(projectId, schemaName, modelName, null) + ":getPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    // 设置模型策略
    // 限流：每用户每秒最多 10 次请求
    public Policy setModelPolicy(String projectId, String schemaName, String modelName, SetPolicyRequest policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getModelPath(projectId, schemaName, modelName, null) + ":setPolicy";
        java.util.Map<String, String> query = new java.util.HashMap<>();
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    /**
     * <b>description</b> :
     * <p>搜索指定 namespace 下的各种实体。</p>
     * 
     * @param namespaceId 主账号ID，在该主账号范围内执行搜索。
     * @param query 搜索查询串，由 1 个到多个查询条件组成，查询条件之间用逗号 `,` 分隔。
     *  - 语法示例：`name:foo,type=TABLE,region=cn-hangzhou`、`description:bar,type=RESOURCE,project=proj`
     *  - 查询条件列表：
     *    1. `name:foo`：将 `foo` 作为子字符串与实体名称匹配。
     *    2. `description:bar`：将 `bar` 作为子字符串与实体描述匹配。
     *    3. `type=TABLE`：匹配特定类型的实体（必选）。当前支持 `TABLE`、`RESOURCE`、`SCHEMA`。
     *    4. `project=proj`：仅搜索指定单个 project 下的查询条件。要求调用方拥有该 project 的 `SearchProject` 权限。
     *    5. `project=(proj1|proj2|proj3)`：搜索多个 project 下的实体（最多 512 个）。要求调用方同时拥有这些 projects 的 `SearchProject` 权限。
     *    6. `region=region_id`：搜索指定 region 的 project 下的实体。
     *  - 约束：
     *    - 查询条件 3 必选。
     *    - 查询条件 4 与查询条件 5 不能同时存在。
     *    - 查询条件 6 不能与查询条件 4 或 5 同时存在。
     * @param pageSize 每页返回结果条数。
     *  - 必须 > 0
     *  - 最大 100
     * @param pageToken 翻页 token；用于从上一次响应的 token 继续获取下一页。
     * @param orderBy 结果排序方式。可取值包括：
     *  - `default`：内部存储顺序（默认）
     *  - `create_time asc`：创建时间正序
     *  - `create_time desc`：创建时间倒序
     *  - `last_modified_time asc`：最近修改时间正序
     *  - `last_modified_time desc`：最近修改时间倒序
     */
    // 限流：每用户每秒最多 10 次请求
    public SearchResponse search(String namespaceId, String query, Integer pageSize, String pageToken, String orderBy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespaceId + ":search";
        java.util.Map<String, String> params = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            params.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            params.put("pageToken", pageToken);
        }

        if (!com.aliyun.teautil.Common.isUnset(query)) {
            params.put("query", com.aliyun.odps.utils.TeaUtils.toString(query));
        }

        if (!com.aliyun.teautil.Common.isUnset(orderBy)) {
            params.put("orderBy", com.aliyun.odps.utils.TeaUtils.toString(orderBy));
        }

        return TeaModel.toModel(this.requestWithModel(new SearchResponse(), "POST", path, params, runtime), new SearchResponse());
    }

    // 限流：每用户每秒最多 100 次请求
    public DataToken getDataToken(Table table, Integer duration) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTablePath(table);
        String fullPath = "" + path + ":getDataToken";
        java.util.Map<String, String> params = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(duration)) {
            params.put("duration", com.aliyun.odps.utils.TeaUtils.toString(duration));
        }

        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", fullPath, params, runtime), new DataToken());
    }
}
