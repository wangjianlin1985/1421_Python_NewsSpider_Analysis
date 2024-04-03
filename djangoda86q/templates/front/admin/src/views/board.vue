<template>
<div class="content box5" :style='{"alignContent":"flex-start","minHeight":"100vh","flexWrap":"wrap","background":"#000","display":"flex","width":"100%","position":"relative","height":"auto"}'>
	<!-- 标题 -->
	<div :style='{"margin":"0 0 30px 0","color":"#fff","textAlign":"center","background":"url(http://codegen.caihongy.cn/20230311/01ae518765ba4240970fb7c150b3e79f.gif) no-repeat center top / 100% 100%","width":"100%","lineHeight":"56px","fontSize":"28px","height":"56px"}'>欢迎使用 {{this.$project.projectName}}</div>
	<!-- 时间 -->
	<div :style='{"top":"0","color":"#fff","display":"inline-block","lineHeight":"64px","fontSize":"16px","position":"absolute","right":"20px","height":"64px"}' class="times">{{ dates }}</div>
	<!-- 系统简介 -->
	<div v-if="systemIntroductionDetail" :style='{"padding":"0px","margin":"0 1% 30px 3%","flexWrap":"wrap","background":"rgba(255,255,255,0)","flexDirection":"column","display":"flex","width":"21%","height":"auto"}'>
		<el-carousel :style='{"width":"100%","margin":"0 auto 10px","height":"200px"}' trigger="click" indicator-position="inside" arrow="always" type="default" direction="horizontal" height="200px" :autoplay="true" :interval="3000" :loop="true">
			<el-carousel-item :style='{"borderRadius":"10px","width":"100%","height":"100%"}' v-if="systemIntroductionDetail.picture1">
				<el-image :style='{"width":"100%","objectFit":"cover","borderRadius":"10px","height":"100%"}' :src="$base.url+ systemIntroductionDetail.picture1" fit="cover"></el-image>
			</el-carousel-item>
			<el-carousel-item :style='{"borderRadius":"10px","width":"100%","height":"100%"}' v-if="systemIntroductionDetail.picture2">
				<el-image :style='{"width":"100%","objectFit":"cover","borderRadius":"10px","height":"100%"}' :src="$base.url+ systemIntroductionDetail.picture2" fit="cover"></el-image>
			</el-carousel-item>
			<el-carousel-item :style='{"borderRadius":"10px","width":"100%","height":"100%"}' v-if="systemIntroductionDetail.picture3">
				<el-image :style='{"width":"100%","objectFit":"cover","borderRadius":"10px","height":"100%"}' :src="$base.url+ systemIntroductionDetail.picture3" fit="cover"></el-image>
			</el-carousel-item>
		</el-carousel>
		<div :style='{"padding":"10px","margin":"10px  0 0 ","overflow":"hidden","color":"#fff","background":"url(http://codegen.caihongy.cn/20230311/87a196fd662648f2ba1c28604018c54c.png) no-repeat center top / 100% 100%","lineHeight":"25px","fontSize":"14px","textIndent":"2em","height":"200px"}' v-html="systemIntroductionDetail.content"></div>
	</div>
	<!-- 统计 -->
	<div :style='{"alignContent":"flex-start","padding":"20px","margin":"0px 1% 20px 1%","flexWrap":"wrap","background":"url(http://codegen.caihongy.cn/20230311/f62ef9465b9048f690fa4f17b534c2e5.gif) no-repeat center top / 100% 100%","display":"flex","width":"23%","height":"420px"}'>
<!-- 1 -->

		<div :style='{"width":"100%","margin":"0 0 20px","alignItems":"center","background":"rgba(255,255,255,.1)","justifyContent":"center","display":"flex"}'>
			<div :style='{"width":"32px","background":"red","display":"none","height":"32px"}'></div>
			<div :style='{"padding":"0 20px","alignItems":"center","flex":"1","justifyContent":"space-between","display":"flex"}'>
				<div :style='{"lineHeight":"32px","fontSize":"15px","color":"#fff","height":"32px"}'>用户总数</div>
				<div :style='{"lineHeight":"32px","fontSize":"20px","color":"#fff","fontWeight":"bold","height":"32px"}'>{{yonghuCount}}</div>
			</div>
		</div>

<!-- 2 -->

		<div :style='{"width":"100%","margin":"0 0 20px","alignItems":"center","background":"rgba(255,255,255,.2)","justifyContent":"center","display":"flex"}'>
			<div :style='{"width":"32px","background":"yellow","display":"none","height":"32px"}'></div>
			<div :style='{"padding":"0 20px","alignItems":"center","flex":"1","justifyContent":"space-between","display":"flex"}'>
				<div :style='{"lineHeight":"32px","fontSize":"15px","color":"#fff","height":"32px"}'>新闻资讯总数</div>
				<div :style='{"lineHeight":"32px","fontSize":"20px","color":"#fff","fontWeight":"bold","height":"32px"}'>{{xinwenzixunCount}}</div>
			</div>
		</div>

<!-- 3 -->

		<div :style='{"width":"100%","margin":"0 0 20px","alignItems":"center","background":"rgba(255,255,255,.1)","justifyContent":"center","display":"flex"}'>
			<div :style='{"width":"32px","background":"red","display":"none","height":"32px"}'></div>
			<div :style='{"padding":"0 20px","alignItems":"center","flex":"1","justifyContent":"space-between","display":"flex"}'>
				<div :style='{"lineHeight":"32px","fontSize":"15px","color":"#fff","height":"32px"}'>网易新闻总数</div>
				<div :style='{"lineHeight":"32px","fontSize":"20px","color":"#fff","fontWeight":"bold","height":"32px"}'>{{wangyixinwenCount}}</div>
			</div>
		</div>

	</div>

	<div class="tables">
		<div :style='{"margin":"0 0 20px 0","color":"#fff","textAlign":"center","background":"rgba(255,255,255,.1)","width":"100%","lineHeight":"64px","fontSize":"28px","height":"64px"}'>网易新闻(跟帖TOP10)</div>
        <el-table :data="boardDataList" border :stripe="false" :style='{"width":"100%","padding":"0","borderColor":"#333","borderStyle":"solid","borderWidth":"1px 0 0 1px","background":"none"}'>
          <el-table-column :resizable="true" :sortable="true" prop="laiyuan" label="来源"/>
          </el-table-column>
          <el-table-column :resizable="true" :sortable="true" prop="biaoti" label="标题"/>
          </el-table-column>
          <el-table-column :resizable="true" :sortable="true" prop="laizi" label="来自"/>
          </el-table-column>
          <el-table-column :resizable="true" :sortable="true" prop="gentie" label="跟帖"/>
          </el-table-column>
          <el-table-column :resizable="true" :sortable="true" prop="guanjianzi" label="关键字"/>
          </el-table-column>
          <el-table-column :resizable="true" :sortable="true" prop="fabushijian" label="发布时间"/>
          </el-table-column>
        </el-table>
	</div>
	
	<div class="echarts1">
		<div id="wangyixinwenChart1" style="width:100%;height:100%;"></div>
	</div>
	<div class="echarts2">
		<div id="wangyixinwenChart2" style="width:100%;height:100%;"></div>
	</div>
	<div class="echarts3">
		<div id="wangyixinwenChart3" style="width:100%;height:100%;"></div>
	</div>
	<div class="echarts4">
		<div id="xinwenzixunChart4" style="width:100%;height:100%;"></div>
	</div>
	<div class="echarts5">
		<div id="wangyixinwenChart5" style="width:100%;height:100%;"></div>
	</div>

</div>


</template>
<script>
import * as echarts from 'echarts'
//3
//5
import router from '@/router/router-static'
export default {
	data() {
		return {
			line: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#fff","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#ccc","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(250,250,250,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#fff","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(255,255,255,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#7bbfea","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"padding":5,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":25,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"left":"100","containLabel":true},"series":{"symbol":"emptyCircle","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#fff","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"showSymbol":true,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"","shadowBlur":0,"width":2,"type":"solid","opacity":1,"shadowColor":"#000"},"symbolSize":4},"title":{"borderType":"solid","padding":2,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"}},
			bar: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#fff","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":10,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal"},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#ccc","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(250,250,250,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#fff","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(255,255,255,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#5470c6","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"padding":5,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":25,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"left":100,"containLabel":true},"series":{"symbol":"emptyCircle","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#fff","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"showSymbol":true,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"","shadowBlur":0,"width":2,"type":"solid","opacity":1,"shadowColor":"#000"},"symbolSize":4},"title":{"borderType":"solid","padding":2,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"},"base":{"animate":true,"interval":3000}},
			pie: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#fff","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#ccc","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(250,250,250,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#fff","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(255,255,255,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#5470c6","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":25,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"left":"100","containLabel":true},"series":{"symbol":"emptyCircle","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#fff","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"showSymbol":true,"top":40,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"","shadowBlur":0,"width":2,"type":"solid","opacity":1,"shadowColor":"#000"},"symbolSize":4},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"}},
			myChart0: null,
			boardDataList: [],
            systemIntroductionDetail: null,
			dates: '',
            yonghuCount: 0,
            xinwenzixunCount: 0,
            wangyixinwenCount: 0,
		};
	},
  mounted(){
    this.init();
    this.getDataList();
    this.getyonghuCount();
    this.getxinwenzixunCount();
    this.xinwenzixunChat4();
    this.getwangyixinwenCount();
    this.wangyixinwenChat1();
    this.wangyixinwenChat2();
    this.wangyixinwenChat3();
    this.wangyixinwenChat5();
  },
  created() {
    this.$nextTick(()=>{
		this.times()
	})
  },
  methods:{
	myChartInterval(type, xAxisData, seriesData, myChart) {
	  this.$nextTick(() => {
	    setInterval(() => {
	      let xAxis = xAxisData.shift()
	      xAxisData.push(xAxis)
	      let series = seriesData.shift()
	      seriesData.push(series)
			
			if (type == 1) {
				myChart.setOption({
				  xAxis: [{
				    data: xAxisData
				  }],
				  series: [{
				    data: seriesData
				  }]
				});
			}
			if (type == 2) {
				myChart.setOption({
				  yAxis: [{
				    data: xAxisData
				  }],
				  series: [{
				    data: seriesData
				  }]
				});
			}
	    }, 3000);
	  })
	},
    getDataList() {
      let params = {
        page: 1,
        limit: 10,
        sort: 'gentie',
        order: 'desc',
      }
      this.$http({
        url: "wangyixinwen/page",
        method: "get",
        params: params
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.boardDataList = data.data.list;
        }
      });
    },
	wordclouds(wordcloudData,echartsId) {
		let wordcloud = {"maskImage":"data:image/png;base64,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","option":{"tooltip":{"show":false},"backgroundColor":"transparent","series":[{"sizeRange":[9,32],"layoutAnimation":true,"shape":"circle","data":[{"name":"花鸟市场","value":1446},{"name":"汽车","value":928},{"name":"视频","value":906},{"name":"电视","value":825},{"name":"Lover Boy 88","value":514},{"name":"动漫","value":486},{"name":"音乐","value":53},{"name":"直播","value":163},{"name":"广播电台","value":86},{"name":"戏曲曲艺","value":17},{"name":"演出票务","value":6},{"name":"给陌生的你听","value":1},{"name":"资讯","value":1437},{"name":"商业财经","value":422},{"name":"娱乐八卦","value":353},{"name":"军事","value":331},{"name":"科技资讯","value":313},{"name":"社会时政","value":307},{"name":"时尚","value":43},{"name":"网络奇闻","value":15},{"name":"旅游出行","value":438},{"name":"景点类型","value":957},{"name":"国内游","value":927},{"name":"远途出行方式","value":908},{"name":"酒店","value":693},{"name":"关注景点","value":611},{"name":"旅游网站偏好","value":512},{"name":"出国游","value":382},{"name":"交通票务","value":312},{"name":"旅游方式","value":187},{"name":"旅游主题","value":163},{"name":"港澳台","value":104},{"name":"本地周边游","value":3},{"name":"小卖家","value":1331},{"name":"全日制学校","value":941},{"name":"基础教育科目","value":585},{"name":"考试培训","value":473},{"name":"语言学习","value":358},{"name":"留学","value":246},{"name":"K12课程培训","value":207},{"name":"艺术培训","value":194},{"name":"技能培训","value":104},{"name":"IT培训","value":87},{"name":"高等教育专业","value":63},{"name":"家教","value":48},{"name":"体育培训","value":23},{"name":"职场培训","value":5},{"name":"金融财经","value":1328},{"name":"银行","value":765},{"name":"股票","value":452},{"name":"保险","value":415},{"name":"贷款","value":253},{"name":"基金","value":211},{"name":"信用卡","value":180},{"name":"外汇","value":138},{"name":"P2P","value":116},{"name":"贵金属","value":98},{"name":"债券","value":93},{"name":"网络理财","value":92},{"name":"信托","value":90},{"name":"征信","value":76},{"name":"期货","value":76},{"name":"公积金","value":40},{"name":"银行理财","value":36},{"name":"银行业务","value":30},{"name":"典当","value":7},{"name":"海外置业","value":1},{"name":"汽车","value":1309},{"name":"汽车档次","value":965},{"name":"汽车品牌","value":900},{"name":"汽车车型","value":727},{"name":"购车阶段","value":461},{"name":"二手车","value":309},{"name":"汽车美容","value":260},{"name":"新能源汽车","value":173},{"name":"汽车维修","value":155},{"name":"租车服务","value":136},{"name":"车展","value":121},{"name":"违章查询","value":76},{"name":"汽车改装","value":62},{"name":"汽车用品","value":37},{"name":"路况查询","value":32},{"name":"汽车保险","value":28},{"name":"陪驾代驾","value":4},{"name":"网络购物","value":1275},{"name":"做我的猫","value":1088},{"name":"只想要你知道","value":907},{"name":"团购","value":837},{"name":"比价","value":201},{"name":"海淘","value":195},{"name":"移动APP购物","value":179},{"name":"支付方式","value":119},{"name":"代购","value":43},{"name":"体育健身","value":1234},{"name":"体育赛事项目","value":802},{"name":"运动项目","value":405},{"name":"体育类赛事","value":337},{"name":"健身项目","value":199},{"name":"健身房健身","value":78},{"name":"运动健身","value":77},{"name":"家庭健身","value":36},{"name":"健身器械","value":29},{"name":"办公室健身","value":3},{"name":"商务服务","value":1201},{"name":"法律咨询","value":508},{"name":"化工材料","value":147},{"name":"广告服务","value":125},{"name":"会计审计","value":115},{"name":"人员招聘","value":101},{"name":"印刷打印","value":66},{"name":"知识产权","value":32},{"name":"翻译","value":22},{"name":"安全安保","value":9},{"name":"公关服务","value":8},{"name":"商旅服务","value":2},{"name":"展会服务","value":2},{"name":"特许经营","value":1},{"name":"休闲爱好","value":1169},{"name":"收藏","value":412},{"name":"摄影","value":393},{"name":"温泉","value":230},{"name":"博彩彩票","value":211},{"name":"美术","value":207},{"name":"书法","value":139},{"name":"DIY手工","value":75},{"name":"舞蹈","value":23},{"name":"钓鱼","value":21},{"name":"棋牌桌游","value":17},{"name":"KTV","value":6},{"name":"密室","value":5},{"name":"采摘","value":4},{"name":"电玩","value":1},{"name":"真人CS","value":1},{"name":"轰趴","value":1},{"name":"家电数码","value":1111},{"name":"手机","value":885},{"name":"电脑","value":543},{"name":"大家电","value":321},{"name":"家电关注品牌","value":253},{"name":"网络设备","value":162},{"name":"摄影器材","value":149},{"name":"影音设备","value":133},{"name":"办公数码设备","value":113},{"name":"生活电器","value":67},{"name":"厨房电器","value":54},{"name":"智能设备","value":45},{"name":"个人护理电器","value":22},{"name":"服饰鞋包","value":1047},{"name":"服装","value":566},{"name":"饰品","value":289},{"name":"鞋","value":184},{"name":"箱包","value":168},{"name":"奢侈品","value":137},{"name":"母婴亲子","value":1041},{"name":"孕婴保健","value":505},{"name":"母婴社区","value":299},{"name":"早教","value":103},{"name":"奶粉辅食","value":66},{"name":"童车童床","value":41},{"name":"关注品牌","value":271},{"name":"宝宝玩乐","value":30},{"name":"母婴护理服务","value":25},{"name":"纸尿裤湿巾","value":16},{"name":"妈妈用品","value":15},{"name":"宝宝起名","value":12},{"name":"童装童鞋","value":9},{"name":"胎教","value":8},{"name":"宝宝安全","value":1},{"name":"宝宝洗护用品","value":1},{"name":"软件应用","value":1018},{"name":"系统工具","value":896},{"name":"理财购物","value":440},{"name":"生活实用","value":365},{"name":"影音图像","value":256},{"name":"社交通讯","value":214},{"name":"手机美化","value":39},{"name":"办公学习","value":28},{"name":"应用市场","value":23},{"name":"母婴育儿","value":14},{"name":"游戏","value":946},{"name":"手机游戏","value":565},{"name":"PC游戏","value":353},{"name":"网页游戏","value":254},{"name":"游戏机","value":188},{"name":"模拟辅助","value":166},{"name":"个护美容","value":942},{"name":"护肤品","value":177},{"name":"彩妆","value":133},{"name":"美发","value":80},{"name":"香水","value":50},{"name":"个人护理","value":46},{"name":"美甲","value":26},{"name":"SPA美体","value":21},{"name":"花鸟萌宠","value":914},{"name":"绿植花卉","value":311},{"name":"狗","value":257},{"name":"其他宠物","value":131},{"name":"水族","value":125},{"name":"猫","value":122},{"name":"动物","value":81},{"name":"鸟","value":67},{"name":"宠物用品","value":41},{"name":"宠物服务","value":26},{"name":"书籍阅读","value":913},{"name":"网络小说","value":483},{"name":"关注书籍","value":128},{"name":"文学","value":105},{"name":"报刊杂志","value":77},{"name":"人文社科","value":22},{"name":"建材家居","value":907},{"name":"装修建材","value":644},{"name":"家具","value":273},{"name":"家居风格","value":187},{"name":"家居家装关注品牌","value":140},{"name":"家纺","value":107},{"name":"厨具","value":47},{"name":"灯具","value":43},{"name":"家居饰品","value":29},{"name":"家居日常用品","value":10},{"name":"生活服务","value":883},{"name":"物流配送","value":536},{"name":"家政服务","value":108},{"name":"摄影服务","value":49},{"name":"搬家服务","value":38},{"name":"物业维修","value":37},{"name":"婚庆服务","value":24},{"name":"二手回收","value":24},{"name":"鲜花配送","value":3},{"name":"维修服务","value":3},{"name":"殡葬服务","value":1},{"name":"求职创业","value":874},{"name":"创业","value":363},{"name":"目标职位","value":162},{"name":"目标行业","value":50},{"name":"兼职","value":21},{"name":"期望年薪","value":20},{"name":"实习","value":16},{"name":"雇主类型","value":10},{"name":"星座运势","value":789},{"name":"星座","value":316},{"name":"算命","value":303},{"name":"解梦","value":196},{"name":"风水","value":93},{"name":"面相分析","value":47},{"name":"手相","value":32},{"name":"公益","value":90}],"keepAspect":false,"type":"wordCloud","rotationRange":[-90,90],"gridSize":8,"shrinkToFit":false,"top":"center","left":"center","width":"80%","emphasis":{"focus":"self","textStyle":{"textShadowColor":"#333","textShadowBlur":4}},"drawOutOfBound":false,"rotationStep":45,"textStyle":{"color":"function(){return\"rgb(\"+[Math.round(160*Math.random()),Math.round(160*Math.random()),Math.round(160*Math.random())].join(\",\")+\")\"}","fontWeight":500,"fontFamily":"sans-serif"},"height":"80%","maskImage":{}}]}}
		wordcloud = JSON.parse(JSON.stringify(wordcloud), (k, v) => {
		  if(typeof v == 'string' && v.indexOf('function') > -1){
		    return eval("(function(){return "+v+" })()")
		  }
		  return v;
		})
		wordcloud.option.series[0].data=wordcloudData;
		
		this.myChart0 = echarts.init(document.getElementById(echartsId));
		let myChart = this.myChart0
		let img = wordcloud.maskImage
	
		if (img) {
			var maskImage = new Image();
			maskImage.src = img
			maskImage.onload = function() {
				wordcloud.option.series[0].maskImage = maskImage
				myChart.clear()
				myChart.setOption(wordcloud.option)
			}
		} else {
			delete wordcloud.option.series[0].maskImage
			myChart.clear()
			myChart.setOption(wordcloud.option)
		}
	},
    getTimeStrToDay(game_over_timestamp) {
        if (game_over_timestamp == 0)
            return "";
        var date = new Date(parseInt(game_over_timestamp));
        var now = new Date();
        var hours = date.getHours() >= 10 ? date.getHours().toString() : "0" + date.getHours();
        var minutes = date.getMinutes() >= 10 ? date.getMinutes().toString() : "0" + date.getMinutes();
        var seconds = date.getSeconds() >= 10 ? date.getSeconds().toString() : "0" + date.getSeconds();
        let arr = ["日", "一", "二", "三", "四", "五", "六"];
        let d = arr[date.getDay()]
        return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + '日' + ' ' + ' ' + '星期' + d  + ' ' + "  " + hours + ":" + minutes + ":" + seconds
    },
	times() {
		setInterval(()=>{
            let date = new Date().getTime()
            this.dates = this.getTimeStrToDay(date)
		}, 1000)
	},
	filterTime(time) {
	  const date = new Date(time)
	  const Y = date.getFullYear()
	  const M = date.getMonth() + 1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1 
	  const D = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
	  
	  const H = date.getHours() < 10 ? '0' + date.getHours() : date.getHours() // 小时
	  const I = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes() // 分钟
	  const S = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds() // 秒
	  
	  return `${Y}-${M}-${D} ${H}:${I}:${S}`
	},
    getSystemIntroduction() {
        this.$http({
            url: `systemintro/detail/1`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.systemIntroductionDetail = data.data
            }
        })
    },
    init(){
        if(this.$storage.get('Token')){
        this.$http({
            url: `${this.$storage.get('sessionTable')}/session`,
            method: "get"
        }).then(({ data }) => {
            if (data && data.code != 0) {
            router.push({ name: 'login' })
            }
        });
        }else{
            router.push({ name: 'login' })
        }
        this.getSystemIntroduction();
    },
    getyonghuCount() {
        this.$http({
            url: `yonghu/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.yonghuCount = data.data
            }
        })
    },











    getxinwenzixunCount() {
        this.$http({
            url: `xinwenzixun/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.xinwenzixunCount = data.data
            }
        })
    },

//统计接口1
    xinwenzixunChat4() {
      this.$nextTick(()=>{

        var xinwenzixunChart4 = echarts.init(document.getElementById("xinwenzixunChart4"),'macarons');
        this.$http({
            url: "xinwenzixun/group/xinwenleixing",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].xinwenleixing);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].xinwenleixing
                    })
                }
                var option = {};
				let titleObj = this.pie.title
				titleObj.text = '新闻分类占比'
				
				const legendObj = this.pie.legend
				
				let seriesObj = {
					type: 'pie',
					radius: ['25%', '55%'],
					center: ['50%', '60%'],
					data: pArray,
					emphasis: {
						itemStyle: {
							shadowBlur: 10,
							shadowOffsetX: 0,
							shadowColor: 'rgba(0, 0, 0, 0.5)'
						}
					}
				}
				seriesObj = Object.assign(seriesObj , this.pie.series)
				
                option = {
					backgroundColor: this.pie.backgroundColor,
					color: this.pie.color,
					title: titleObj,
					legend: legendObj,
					tooltip: {
						trigger: 'item',
						formatter: '{b} : {c} ({d}%)'
					},
					series: [seriesObj]
                };
                // 使用刚指定的配置项和数据显示图表。
                xinwenzixunChart4.setOption(option);
				

                  //根据窗口的大小变动图表
                window.onresize = function() {
                    xinwenzixunChart4.resize();
                };
            }
        });
      })
    },





















    getwangyixinwenCount() {
        this.$http({
            url: `wangyixinwen/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.wangyixinwenCount = data.data
            }
        })
    },

//统计接口1
    wangyixinwenChat1() {
      this.$nextTick(()=>{
        // biaoti biaoti
        //  gentie

        var wangyixinwenChart1 = echarts.init(document.getElementById("wangyixinwenChart1"),'macarons');
        this.$http({
            url: `wangyixinwen/value/biaoti/gentie`,
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].biaoti);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].biaoti
                    })
                }
                var option = {};
				let titleObj = this.bar.title
				titleObj.text = '跟帖统计'
				
				const legendObj = this.bar.legend
				
				let xAxisObj = this.bar.xAxis
				xAxisObj.type = 'value'
                xAxisObj.axisLabel.rotate=70
				
				let yAxisObj = this.bar.yAxis
				yAxisObj.type = 'category'
				yAxisObj.data = xAxis
				
				let seriesObj = {
                        data: yAxis,
                        type: 'bar'
                    }
				seriesObj = Object.assign(seriesObj , this.bar.series)

                option = {
					backgroundColor: this.bar.backgroundColor,
					color: this.bar.color,
                    title: titleObj,
					legend: legendObj,
                    tooltip: {
						trigger: 'item',
						formatter: '{b} : {c}'
                    },
                    xAxis: xAxisObj,
                    yAxis: yAxisObj,
                    series: [seriesObj]
                };
                // 使用刚指定的配置项和数据显示图表。
                wangyixinwenChart1.setOption(option);
				
				this.myChartInterval(2, option.yAxis.data, option.series[0].data, wangyixinwenChart1)

                  //根据窗口的大小变动图表
                window.onresize = function() {
                    wangyixinwenChart1.resize();
                };
            }
        });
      })
    },

//统计接口2
    wangyixinwenChat2() {
      this.$nextTick(()=>{

        var wangyixinwenChart2 = echarts.init(document.getElementById("wangyixinwenChart2"),'macarons');
        this.$http({
            url: "wangyixinwen/group/guanjianzi",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].guanjianzi);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].guanjianzi
                    })
                }
                var option = {};
                let titleObj = this.bar.title
				titleObj.text = '关键字统计'
				
				const legendObj = this.bar.legend
				
				let xAxisObj = this.bar.xAxis
				xAxisObj.type = 'category'
				xAxisObj.data = xAxis
                xAxisObj.axisLabel.rotate=70
				
				let yAxisObj = this.bar.yAxis
				yAxisObj.type = 'value'
				
				let seriesObj = {
						data: yAxis,
						type: 'bar'
					}
				seriesObj = Object.assign(seriesObj , this.bar.series)

				option = {
					backgroundColor: this.bar.backgroundColor,
					color: this.bar.color,
					title: titleObj,
					legend: legendObj,
					tooltip: {
						trigger: 'item',
						formatter: '{b} : {c}'
					},
					xAxis: xAxisObj,
					yAxis: yAxisObj,
					series: [seriesObj]
				};
                // 使用刚指定的配置项和数据显示图表。
                wangyixinwenChart2.setOption(option);
				
				this.myChartInterval(1, option.xAxis.data, option.series[0].data, wangyixinwenChart2)

                  //根据窗口的大小变动图表
                window.onresize = function() {
                    wangyixinwenChart2.resize();
                };
            }
        });
      })
    },

//统计接口3
    wangyixinwenChat3() {
      this.$nextTick(()=>{

        var wangyixinwenChart3 = echarts.init(document.getElementById("wangyixinwenChart3"),'macarons');
        this.$http({
            url: "wangyixinwen/group/laizi",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].laizi);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].laizi
                    })
                }
                var option = {};
				let titleObj = this.pie.title
				titleObj.text = '来源统计'
				
				const legendObj = this.pie.legend
				
				let seriesObj = {
					type: 'pie',
					radius: '55%',
					center: ['50%', '60%'],
					data: pArray,
					emphasis: {
						itemStyle: {
							shadowBlur: 10,
							shadowOffsetX: 0,
							shadowColor: 'rgba(0, 0, 0, 0.5)'
						}
					}
				}
				seriesObj = Object.assign(seriesObj , this.pie.series)
				
				option = {
					backgroundColor: this.pie.backgroundColor,
					color: this.pie.color,
					title: titleObj,
					legend: legendObj,
					tooltip: {
						trigger: 'item',
						formatter: '{b} : {c} ({d}%)'
					},
					series: [seriesObj]
				};
                // 使用刚指定的配置项和数据显示图表。
                wangyixinwenChart3.setOption(option);
				

                  //根据窗口的大小变动图表
                window.onresize = function() {
                    wangyixinwenChart3.resize();
                };
            }
        });
      })
    },

//统计接口4
    wangyixinwenChat5() {
      this.$nextTick(()=>{

        this.$http({
            url: "group/wangyixinwen/guanjianzi",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].guanjianzi);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].guanjianzi
                    })
                }
                var option = {};
                this.wordclouds(pArray,'wangyixinwenChart5');
				

            }
        });
      })
    },









































































  }
};
</script>
<style lang="scss" scoped>
    .cardView {
        display: flex;
        flex-wrap: wrap;
        width: 100%;

        .cards {
            display: flex;
            align-items: center;
            width: 100%;
            margin-bottom: 10px;
            justify-content: center;
            .card {
                width: calc(25% - 20px);
                margin: 0 10px;
                /deep/.el-card__body{
                    padding: 0;
                }
            }
        }
    }
	
	.box5 .wordcloud {
			}
	.box5 .tables {
				padding: 20px;
				margin: 0 3% 50px 3%;
				background: url(http://codegen.caihongy.cn/20230311/f62ef9465b9048f690fa4f17b534c2e5.gif) no-repeat center top / 100% 100%;
				width: 94%;
				transition: 0.3s;
				height: auto;
				order: 10;
			}
	.box5 .echarts1 {
				padding: 10px;
				margin: 0 3% 30px 1%;
				background: url(http://codegen.caihongy.cn/20230311/f62ef9465b9048f690fa4f17b534c2e5.gif) no-repeat center top / 100% 100%;
				width: 46%;
				transition: 0.3s;
				height: 420px;
			}
	.box5 .echarts2 {
				padding: 10px;
				margin: 0 1% 30px 3%;
				background: url(http://codegen.caihongy.cn/20230311/f62ef9465b9048f690fa4f17b534c2e5.gif) no-repeat center top / 100% 100%;
				width: 46%;
				transition: 0.3s;
				height: 360px;
			}
	.box5 .echarts3 {
				padding: 10px;
				margin: 0 3% 30px 1%;
				background: url(http://codegen.caihongy.cn/20230311/f62ef9465b9048f690fa4f17b534c2e5.gif) no-repeat center top / 100% 100%;
				width: 46%;
				transition: 0.3s;
				height: 360px;
			}
	.box5 .echarts4 {
				padding: 10px;
				margin: 0 1% 30px 3%;
				background: url(http://codegen.caihongy.cn/20230311/f62ef9465b9048f690fa4f17b534c2e5.gif) no-repeat center top / 100% 100%;
				width: 46%;
				transition: 0.3s;
				height: 360px;
			}
	.box5 .echarts5 {
				padding: 10px;
				margin: 0 3% 30px 1%;
				background: url(http://codegen.caihongy.cn/20230311/f62ef9465b9048f690fa4f17b534c2e5.gif) no-repeat center top / 100% 100%;
				width: 46%;
				transition: 0.3s;
				height: 360px;
			}
	
	.box5 .wordcloud:hover {
			}
	.box5 .tables:hover {
			}
	.box5 .echarts1:hover {
			}
	.box5 .echarts2:hover {
			}
	.box5 .echarts3:hover {
			}
	.box5 .echarts4:hover {
			}
	.box5 .echarts5:hover {
			}
	
	// table
	.box5 .el-table /deep/ .el-table__header-wrapper thead {
				color: #ccc;
				font-weight: 500;
				width: 100%;
			}
	
	.box5 .el-table /deep/ .el-table__header-wrapper thead tr {
				background: none;
			}
	
	.box5 .el-table /deep/ .el-table__header-wrapper thead tr th {
				padding: 6px 0;
				background: none;
				border-color: #333;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	.box5 .el-table /deep/ .el-table__header-wrapper thead tr th .cell {
				padding: 0 10px;
				word-wrap: normal;
				word-break: break-all;
				white-space: normal;
				font-weight: bold;
				display: inline-block;
				vertical-align: middle;
				width: 100%;
				line-height: 24px;
				position: relative;
				text-overflow: ellipsis;
			}
	
	.box5 .el-table /deep/ .el-table__body-wrapper tbody {
				width: 100%;
			}
	
	.box5 .el-table /deep/ .el-table__body-wrapper tbody tr {
				background: none;
			}
	
	.box5 .el-table /deep/ .el-table__body-wrapper tbody tr td {
				padding: 6px 0;
				color: #ccc;
				background: none;
				border-color: #333;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
		
	.box5 .el-table /deep/ .el-table__body-wrapper tbody tr:hover td {
				padding: 6px 0;
				color: #ccc;
				background: none;
				border-color: #333;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	.box5 .el-table /deep/ .el-table__body-wrapper tbody tr td {
				padding: 6px 0;
				color: #ccc;
				background: none;
				border-color: #333;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	.box5 .el-table /deep/ .el-table__body-wrapper tbody tr td .cell {
				padding: 0 10px;
				overflow: hidden;
				word-break: break-all;
				white-space: normal;
				line-height: 24px;
				text-overflow: ellipsis;
			}





</style>
