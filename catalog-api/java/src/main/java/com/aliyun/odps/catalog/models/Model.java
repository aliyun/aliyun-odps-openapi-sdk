// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.odps.catalog.models;

import com.aliyun.tea.*;

/**
 * <b>description</b> :
 * <p>==================================== Models ====================================</p>
 */
public class Model extends TeaModel {
    /**
     * <p>模型的完整路径。e.g., projects/{projectId}/schemas/{schemaName}/models/{modelName}</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>模型名。上级 Schema 内唯一。大小写不敏感。包含字符：[a-z][A-Z][0-9]_，字节个数范围 [3, 255]</p>
     */
    @NameInMap("modelName")
    public String modelName;

    /**
     * <p>版本名。同一 model 范围内唯一。大小写不敏感。包含字符：[a-z][A-Z][0-9]_，字节个数范围 [3, 255]</p>
     */
    @NameInMap("versionName")
    public String versionName;

    /**
     * <p>模型的默认版本名</p>
     */
    @NameInMap("defaultVersion")
    public String defaultVersion;

    /**
     * <p>模型的创建时间（毫秒）</p>
     */
    @NameInMap("createTime")
    public String createTime;

    /**
     * <p>模型的修改时间（毫秒）</p>
     */
    @NameInMap("updateTime")
    public String updateTime;

    /**
     * <p>版本的创建时间（毫秒）</p>
     */
    @NameInMap("versionCreateTime")
    public String versionCreateTime;

    /**
     * <p>版本的修改时间（毫秒）</p>
     */
    @NameInMap("versionUpdateTime")
    public String versionUpdateTime;

    /**
     * <p>模型的描述，最长 1KB</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>版本的描述，最长 1KB</p>
     */
    @NameInMap("versionDescription")
    public String versionDescription;

    /**
     * <p>模型基于最近更新时间的生命周期（天）</p>
     */
    @NameInMap("expirationDays")
    public Integer expirationDays;

    /**
     * <p>版本基于最近更新时间的生命周期（天）</p>
     */
    @NameInMap("versionExpirationDays")
    public Integer versionExpirationDays;

    /**
     * <p>模型的来源类型，创建后不支持修改</p>
     */
    @NameInMap("sourceType")
    public String sourceType;

    /**
     * <p>模型的类型，创建后不支持修改</p>
     */
    @NameInMap("modelType")
    public String modelType;

    /**
     * <p>模型的标签</p>
     */
    @NameInMap("labels")
    public java.util.Map<String, String> labels;

    /**
     * <p>版本的预处理信息</p>
     */
    @NameInMap("transform")
    public java.util.Map<String, String> transform;

    /**
     * <p>版本对应模型文件的路径</p>
     */
    @NameInMap("path")
    public String path;

    /**
     * <p>版本的参数</p>
     */
    @NameInMap("options")
    public java.util.Map<String, String> options;

    /**
     * <p>模型的额外信息</p>
     */
    @NameInMap("extraInfo")
    public java.util.Map<String, String> extraInfo;

    /**
     * <p>版本的额外信息</p>
     */
    @NameInMap("versionExtraInfo")
    public java.util.Map<String, String> versionExtraInfo;

    /**
     * <p>版本的训练信息</p>
     */
    @NameInMap("trainingInfo")
    public java.util.Map<String, String> trainingInfo;

    /**
     * <p>版本的推理参数</p>
     */
    @NameInMap("inferenceParameters")
    public java.util.Map<String, String> inferenceParameters;

    /**
     * <p>版本的列 schema 定义</p>
     */
    @NameInMap("featureColumns")
    public ModelFieldSchema featureColumns;

    /**
     * <p>version 支持的所有 task 类型。要求：对于 LLM/MLLM 类型模型，可取值 text-generation，chat，sentence-embedding 中的一个或多个. 对于 BOOSTED_TREE_CLASSIFIER 类型模型，只能取值为 [predict, predict-proba, feature-importance]（顺序任意）. 对于 BOOSTED_TREE_REGRESSOR 类型模型，只能取值为 [predict, feature-importance]（顺序任意）</p>
     */
    @NameInMap("tasks")
    public java.util.List<String> tasks;

    public static Model build(java.util.Map<String, ?> map) throws Exception {
        Model self = new Model();
        return TeaModel.build(map, self);
    }

    public Model setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public Model setModelName(String modelName) {
        this.modelName = modelName;
        return this;
    }
    public String getModelName() {
        return this.modelName;
    }

    public Model setVersionName(String versionName) {
        this.versionName = versionName;
        return this;
    }
    public String getVersionName() {
        return this.versionName;
    }

    public Model setDefaultVersion(String defaultVersion) {
        this.defaultVersion = defaultVersion;
        return this;
    }
    public String getDefaultVersion() {
        return this.defaultVersion;
    }

    public Model setCreateTime(String createTime) {
        this.createTime = createTime;
        return this;
    }
    public String getCreateTime() {
        return this.createTime;
    }

    public Model setUpdateTime(String updateTime) {
        this.updateTime = updateTime;
        return this;
    }
    public String getUpdateTime() {
        return this.updateTime;
    }

    public Model setVersionCreateTime(String versionCreateTime) {
        this.versionCreateTime = versionCreateTime;
        return this;
    }
    public String getVersionCreateTime() {
        return this.versionCreateTime;
    }

    public Model setVersionUpdateTime(String versionUpdateTime) {
        this.versionUpdateTime = versionUpdateTime;
        return this;
    }
    public String getVersionUpdateTime() {
        return this.versionUpdateTime;
    }

    public Model setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public Model setVersionDescription(String versionDescription) {
        this.versionDescription = versionDescription;
        return this;
    }
    public String getVersionDescription() {
        return this.versionDescription;
    }

    public Model setExpirationDays(Integer expirationDays) {
        this.expirationDays = expirationDays;
        return this;
    }
    public Integer getExpirationDays() {
        return this.expirationDays;
    }

    public Model setVersionExpirationDays(Integer versionExpirationDays) {
        this.versionExpirationDays = versionExpirationDays;
        return this;
    }
    public Integer getVersionExpirationDays() {
        return this.versionExpirationDays;
    }

    public Model setSourceType(String sourceType) {
        this.sourceType = sourceType;
        return this;
    }
    public String getSourceType() {
        return this.sourceType;
    }

    public Model setModelType(String modelType) {
        this.modelType = modelType;
        return this;
    }
    public String getModelType() {
        return this.modelType;
    }

    public Model setLabels(java.util.Map<String, String> labels) {
        this.labels = labels;
        return this;
    }
    public java.util.Map<String, String> getLabels() {
        return this.labels;
    }

    public Model setTransform(java.util.Map<String, String> transform) {
        this.transform = transform;
        return this;
    }
    public java.util.Map<String, String> getTransform() {
        return this.transform;
    }

    public Model setPath(String path) {
        this.path = path;
        return this;
    }
    public String getPath() {
        return this.path;
    }

    public Model setOptions(java.util.Map<String, String> options) {
        this.options = options;
        return this;
    }
    public java.util.Map<String, String> getOptions() {
        return this.options;
    }

    public Model setExtraInfo(java.util.Map<String, String> extraInfo) {
        this.extraInfo = extraInfo;
        return this;
    }
    public java.util.Map<String, String> getExtraInfo() {
        return this.extraInfo;
    }

    public Model setVersionExtraInfo(java.util.Map<String, String> versionExtraInfo) {
        this.versionExtraInfo = versionExtraInfo;
        return this;
    }
    public java.util.Map<String, String> getVersionExtraInfo() {
        return this.versionExtraInfo;
    }

    public Model setTrainingInfo(java.util.Map<String, String> trainingInfo) {
        this.trainingInfo = trainingInfo;
        return this;
    }
    public java.util.Map<String, String> getTrainingInfo() {
        return this.trainingInfo;
    }

    public Model setInferenceParameters(java.util.Map<String, String> inferenceParameters) {
        this.inferenceParameters = inferenceParameters;
        return this;
    }
    public java.util.Map<String, String> getInferenceParameters() {
        return this.inferenceParameters;
    }

    public Model setFeatureColumns(ModelFieldSchema featureColumns) {
        this.featureColumns = featureColumns;
        return this;
    }
    public ModelFieldSchema getFeatureColumns() {
        return this.featureColumns;
    }

    public Model setTasks(java.util.List<String> tasks) {
        this.tasks = tasks;
        return this;
    }
    public java.util.List<String> getTasks() {
        return this.tasks;
    }

}
