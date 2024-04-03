const base = {
    get() {
        return {
            url : "http://localhost:8080/djangoda86q/",
            name: "djangoda86q",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于python的网易新闻数据分析与可视化"
        } 
    }
}
export default base
