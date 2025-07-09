// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog;

import com.aliyun.tea.*;
import com.aliyun.odps.catalog.models.*;

public class Client extends com.aliyun.odps.Client {

    public Client(com.aliyun.odps.models.Config config) throws Exception {
        super(config);
    }


    public Table updateTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(table, "PUT", this.getTablePath(table), null, runtime), new Table());
    }

    public HttpResponse deleteTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithoutModel(table, "DELETE", this.getTablePath(table), null, runtime), new HttpResponse());
    }

    public Table createTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(table, "POST", this.getTablesPath(table), null, runtime), new Table());
    }

    public Table getTable(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(table, "GET", this.getTablePath(table), null, runtime), new Table());
    }

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

    public Policy setTablePolicy(Table table, Policy policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTablePath(table);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "getPolicy");
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    public Policy getTablePolicy(Table table) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTablePath(table);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "getPolicy");
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

    public Connection createConnection(String namespace, Connection connection) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespace + "/connections";
        return TeaModel.toModel(this.requestWithModel(connection, "POST", path, null, runtime), new Connection());
    }

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

    public Connection getConnection(String namespace, String connectionName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getConnectionPath(namespace, connectionName);
        return TeaModel.toModel(this.requestWithModel(new Connection(), "GET", path, null, runtime), new Connection());
    }

    public Connection updateConnection(String namespace, String connectionName, Connection connection, String updateMask) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getConnectionPath(namespace, connectionName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("updateMask", updateMask);
        return TeaModel.toModel(this.requestWithModel(connection, "PATCH", path, query, runtime), new Connection());
    }

    public HttpResponse deleteConnection(String namespace, String connectionName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getConnectionPath(namespace, connectionName);
        return TeaModel.toModel(this.requestWithoutModel(new Connection(), "DELETE", path, null, runtime), new HttpResponse());
    }

    public Policy setConnectionPolicy(String namespace, String connectionName, SetPolicyRequest request) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getConnectionPath(namespace, connectionName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "setPolicy");
        return TeaModel.toModel(this.requestWithModel(request, "POST", path, query, runtime), new Policy());
    }

    public Policy getConnectionPolicy(String namespace, String connectionName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getConnectionPath(namespace, connectionName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "getPolicy");
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
    public Role createRole(String namespace, Role role) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespace + "/roles";
        return TeaModel.toModel(this.requestWithModel(role, "POST", path, null, runtime), new Role());
    }

    // Delete role
    public HttpResponse deleteRole(String namespace, String roleName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getRolePath(namespace, roleName);
        return TeaModel.toModel(this.requestWithoutModel(new Role(), "DELETE", path, null, runtime), new HttpResponse());
    }

    // Get role
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
    public Role patchRole(String namespace, String roleName, Role role, String updateMask) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getRolePath(namespace, roleName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(updateMask)) {
            query.put("updateMask", updateMask);
        }

        return TeaModel.toModel(this.requestWithModel(role, "PATCH", path, query, runtime), new Role());
    }

    // Set role policy
    public Policy setRolePolicy(String namespace, String roleName, Policy policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getRolePath(namespace, roleName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "setPolicy");
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    // Get role policy
    public Policy getRolePolicy(String namespace, String roleName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getRolePath(namespace, roleName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "getPolicy");
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
    public Taxonomy createTaxonomy(String namespace, Taxonomy taxonomy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/namespaces/" + namespace + "/taxonomies";
        return TeaModel.toModel(this.requestWithModel(taxonomy, "POST", path, null, runtime), new Taxonomy());
    }

    public HttpResponse deleteTaxonomy(String namespace, String taxonomyId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTaxonomyPath(namespace, taxonomyId);
        return TeaModel.toModel(this.requestWithoutModel(new Taxonomy(), "DELETE", path, null, runtime), new HttpResponse());
    }

    public Taxonomy getTaxonomy(String namespace, String taxonomyId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTaxonomyPath(namespace, taxonomyId);
        return TeaModel.toModel(this.requestWithModel(new Taxonomy(), "GET", path, null, runtime), new Taxonomy());
    }

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

    public Taxonomy patchTaxonomy(String namespace, String taxonomyId, Taxonomy taxonomy, String updateMask) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTaxonomyPath(namespace, taxonomyId);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(updateMask)) {
            query.put("updateMask", updateMask);
        }

        return TeaModel.toModel(this.requestWithModel(taxonomy, "PATCH", path, query, runtime), new Taxonomy());
    }

    public Policy setTaxonomyPolicy(String namespace, String taxonomyId, Policy policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTaxonomyPath(namespace, taxonomyId);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "setPolicy");
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    public Policy getTaxonomyPolicy(String namespace, String taxonomyId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTaxonomyPath(namespace, taxonomyId);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "getPolicy");
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    // PolicyTag operations
    public PolicyTag createPolicyTag(String namespace, String taxonomyId, PolicyTag policyTag) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "" + this.getTaxonomyPath(namespace, taxonomyId) + "/policyTags";
        return TeaModel.toModel(this.requestWithModel(policyTag, "POST", path, null, runtime), new PolicyTag());
    }

    public HttpResponse deletePolicyTag(String namespace, String taxonomyId, String policyTagId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getPolicyTagPath(namespace, taxonomyId, policyTagId);
        return TeaModel.toModel(this.requestWithoutModel(new PolicyTag(), "DELETE", path, null, runtime), new HttpResponse());
    }

    public PolicyTag getPolicyTag(String namespace, String taxonomyId, String policyTagId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getPolicyTagPath(namespace, taxonomyId, policyTagId);
        return TeaModel.toModel(this.requestWithModel(new PolicyTag(), "GET", path, null, runtime), new PolicyTag());
    }

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

    public PolicyTag patchPolicyTag(String namespace, String taxonomyId, String policyTagId, PolicyTag policyTag, String updateMask) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getPolicyTagPath(namespace, taxonomyId, policyTagId);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(updateMask)) {
            query.put("updateMask", updateMask);
        }

        return TeaModel.toModel(this.requestWithModel(policyTag, "PATCH", path, query, runtime), new PolicyTag());
    }

    public Policy setPolicyTagPolicy(String namespace, String taxonomyId, String policyTagId, Policy policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getPolicyTagPath(namespace, taxonomyId, policyTagId);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "setPolicy");
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    public Policy getPolicyTagPolicy(String namespace, String taxonomyId, String policyTagId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getPolicyTagPath(namespace, taxonomyId, policyTagId);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "getPolicy");
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    public DataPolicy createDataPolicy(String namespace, DataPolicy dataPolicy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getParentPath(namespace);
        return TeaModel.toModel(this.requestWithModel(dataPolicy, "POST", path, null, runtime), new DataPolicy());
    }

    public HttpResponse deleteDataPolicy(String namespace, String dataPolicyName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataPolicyPath(namespace, dataPolicyName);
        return TeaModel.toModel(this.requestWithoutModel(new DataPolicy(), "DELETE", path, null, runtime), new HttpResponse());
    }

    public DataPolicy getDataPolicy(String namespace, String dataPolicyName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataPolicyPath(namespace, dataPolicyName);
        return TeaModel.toModel(this.requestWithModel(new DataPolicy(), "GET", path, null, runtime), new DataPolicy());
    }

    public ListDataPoliciesResponse listDataPolicies(String namespace, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getParentPath(namespace);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListDataPoliciesResponse(), "GET", path, query, runtime), new ListDataPoliciesResponse());
    }

    public Policy setDataPolicyPolicy(String namespace, String dataPolicyName, SetPolicyRequest request) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataPolicyPath(namespace, dataPolicyName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "setPolicy");
        return TeaModel.toModel(this.requestWithModel(request, "POST", path, query, runtime), new Policy());
    }

    public Policy getDataPolicyPolicy(String namespace, String dataPolicyName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getDataPolicyPath(namespace, dataPolicyName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "getPolicy");
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    public String getDataPolicyPath(String namespace, String dataPolicyName) throws Exception {
        return "/api/catalog/v1alpha/namespaces/" + namespace + "/dataPolicies/" + dataPolicyName + "";
    }

    public String getParentPath(String namespace) throws Exception {
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

    public Project getProject(String projectId) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(new Project(), "GET", this.getProjectPath(projectId), null, runtime), new Project());
    }

    public Schema createSchema(String projectId, Schema schema) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = "/api/catalog/v1alpha/projects/" + projectId + "/schemas";
        return TeaModel.toModel(this.requestWithModel(schema, "POST", path, null, runtime), new Schema());
    }

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

    public Schema getSchema(String projectId, String schemaName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        return TeaModel.toModel(this.requestWithModel(new Schema(), "GET", this.getSchemaPath(projectId, schemaName), null, runtime), new Schema());
    }

    public Schema updateSchema(String projectId, String schemaName, String updateMask, Schema schema) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getSchemaPath(projectId, schemaName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("updateMask", updateMask);
        return TeaModel.toModel(this.requestWithModel(schema, "PATCH", path, query, runtime), new Schema());
    }

    public HttpResponse deleteSchema(String projectId, String schemaName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getSchemaPath(projectId, schemaName);
        return TeaModel.toModel(this.requestWithoutModel(new Schema(), "DELETE", path, null, runtime), new HttpResponse());
    }

    public Policy setSchemaPolicy(String projectId, String schemaName, Policy policy) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getSchemaPath(projectId, schemaName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "setPolicy");
        return TeaModel.toModel(this.requestWithModel(policy, "POST", path, query, runtime), new Policy());
    }

    public Policy getSchemaPolicy(String projectId, String schemaName) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getSchemaPath(projectId, schemaName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        query.put("method", "getPolicy");
        return TeaModel.toModel(this.requestWithModel(new Policy(), "POST", path, query, runtime), new Policy());
    }

    // Path Functions
    public String getTablePartitionsPath(String projectId, String schemaName, String tableName) throws Exception {
        return "/api/catalog/v1alpha/projects/" + projectId + "/schemas/" + schemaName + "/tables/" + tableName + "/partitions";
    }

    // Methods
    public ListPartitionsResponse listPartitions(String projectId, String schemaName, String tableName, Integer pageSize, String pageToken) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        String path = this.getTablePartitionsPath(projectId, schemaName, tableName);
        java.util.Map<String, String> query = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(pageSize)) {
            query.put("pageSize", com.aliyun.odps.utils.TeaUtils.toString(pageSize));
        }

        if (!com.aliyun.teautil.Common.isUnset(pageToken)) {
            query.put("pageToken", pageToken);
        }

        return TeaModel.toModel(this.requestWithModel(new ListPartitionsResponse(), "GET", path, query, runtime), new ListPartitionsResponse());
    }
}
