import os

base_dir = "/Users/mahmoudabdelkawy/Desktop/prometheus-grafana-presentation"
input_html = os.path.join(base_dir, "index.html")
out_dir = os.path.join(base_dir, "kubernetes")
os.makedirs(out_dir, exist_ok=True)
out_html = os.path.join(out_dir, "index.html")

with open(input_html, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header
header_end = content.find('<!-- ══ S1: COVER ══ -->')
header = content[:header_end]
# change title
header = header.replace('<title>Prometheus & Grafana — شرح موسّع</title>', '<title>Kubernetes & Minikube — شرح موسّع</title>')

# Extract footer
footer_start = content.rfind('</div>\n\n<script>')
footer = content[footer_start:]

slides = """
<!-- ══ S1: COVER ══ -->
<section class="slide active" id="s1">
  <div class="blob" style="width:500px;height:500px;background:#326ce5;top:-180px;right:-100px"></div>
  <div class="blob" style="width:380px;height:380px;background:#63b3ed;bottom:-120px;left:-80px;animation-delay:3s"></div>
  <div class="badge">☸️ Container Orchestration — شرح موسّع</div>
  <h1><span style="color:#326ce5">Kubernetes</span> <span style="color:var(--mut)">&</span> <span style="color:#63b3ed">Minikube</span></h1>
  <p class="sub">نظام مفتوح المصدر لإدارة الحاويات وأتمتة نشر التطبيقات لضمان توفرها الدائم وتوزيع الأحمال.</p>
  <div class="tags">
    <span class="tag">Kubernetes</span><span class="tag">Minikube</span><span class="tag">Control Plane</span>
    <span class="tag">Worker Nodes</span><span class="tag">Pods</span><span class="tag">Docker</span>
  </div>
</section>

<!-- ══ S2: Architecture ══ -->
<section class="slide" id="s2">
  <div class="blob" style="width:400px;height:400px;background:#326ce5;top:-100px;left:-80px"></div>
  <h2 class="stitle">🏗️ بنية Kubernetes (Architecture)</h2>
  <div class="sline" style="width:70px;background:#326ce5"></div>
  <div class="g2" style="margin-bottom:14px">
    <div class="card">
      <div class="tb" style="background:#326ce5"></div>
      <span class="ico">🧠</span>
      <h3 style="color:#326ce5">لوحة التحكم (Control Plane)</h3>
      <p>العقل المدبر الذي يدير النظام بالكامل. يتخذ القرارات ويراقب حالة العنقود.<br><br>
         • يستقبل الأوامر<br>
         • يجد الموارد المتاحة<br>
         • يراقب استقرار النظام</p>
    </div>
    <div class="card">
      <div class="tb" style="background:#63b3ed"></div>
      <span class="ico">⚙️</span>
      <h3 style="color:#63b3ed">العقد (Worker Nodes)</h3>
      <p>الأجهزة (حقيقية أو افتراضية) التي تعمل عليها التطبيقات (الحاويات) فعلياً.<br><br>
         • تشغل الحاويات<br>
         • توفر موارد الحوسبة<br>
         • تتواصل مع الـ Control Plane</p>
    </div>
  </div>
</section>

<!-- ══ S3: ARCHITECTURE MAP (ROADMAP) ══ -->
<section class="slide" id="s3">
  <div class="blob" style="width:400px;height:400px;background:#9f7aea;top:-100px;right:-80px"></div>
  <h2 class="stitle" style="color:#b794f4">🗺️ الخريطة التوضيحية لعمل Kubernetes</h2>
  <div class="sline" style="width:70px;background:#b794f4"></div>
  <div class="arch" style="margin-bottom:16px">
    <div class="anode" style="border-color:#63b3ed">
      <div class="ani">👨‍💻</div>
      <h4>أنت (User)</h4>
      <p>تستخدم kubectl أو UI</p>
    </div>
    <div class="aconn"><div class="arr">←</div><div class="lbl">YAML / Commands</div></div>
    
    <div class="anode" style="border-color:#326ce5">
      <div class="ani">🧠</div>
      <h4>Control Plane</h4>
      <p>API Server | etcd<br>Scheduler | Controllers</p>
    </div>
    <div class="aconn"><div class="arr">←</div><div class="lbl">Assign / Sync</div></div>
    
    <div class="anode" style="border-color:#68d391">
      <div class="ani">⚙️</div>
      <h4>Worker Node</h4>
      <p>Kubelet | Kube-Proxy</p>
      <span class="port">يشغل الحاويات في Pods</span>
    </div>
  </div>
  <div class="card" style="max-width:900px;width:100%;padding:18px;margin-top:10px;">
    <h3 style="color:#b794f4;font-size:15px;margin-bottom:10px">🔄 قصة حياة أي طلب في Kubernetes:</h3>
    <ul class="dlist">
      <li><span class="li">1️⃣</span><span><strong>أنت تطلب:</strong> `kubectl apply -f pod.yaml` — الطلب يذهب مباشرة إلى الـ <strong>API Server</strong>.</span></li>
      <li><span class="li">2️⃣</span><span><strong>الحفظ:</strong> الـ API Server يراجع الصلاحيات ويحفظ هذا الطلب في الـ <strong>etcd</strong> (ذاكرة العنقود).</span></li>
      <li><span class="li">3️⃣</span><span><strong>التوزيع:</strong> الـ <strong>Scheduler</strong> يلاحظ وجود Pod جديد بلا عنوان، فيبحث عن أفضل <strong>Node</strong> ليضع الـ Pod فيها.</span></li>
      <li><span class="li">4️⃣</span><span><strong>التنفيذ:</strong> الـ <strong>Kubelet</strong> الموجود على الـ Node يقرأ الأوامر من الـ API Server ويطلب من <strong>Docker</strong> تشغيل الحاوية!</span></li>
    </ul>
  </div>
</section>

<!-- ══ S4: Control Plane Details ══ -->
<section class="slide" id="s4">
  <div class="blob" style="width:400px;height:400px;background:var(--acc2);top:-100px;right:-80px"></div>
  <h2 class="stitle">🧠 تفصيل مكونات الـ Control Plane</h2>
  <div class="sline" style="width:70px;background:var(--acc2)"></div>
  <div class="g4" style="margin-bottom:14px">
    <div class="mtype">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--acc)"></div>
      <h4 style="color:var(--acc)">Kube-API Server 🚪</h4>
      <p>البوابة الرئيسية. أي شيء في K8s (حتى المكونات الداخلية) يجب أن تتحدث معه. لا يوجد تواصل مباشر بين المكونات الأخرى.</p>
    </div>
    <div class="mtype">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--grn)"></div>
      <h4 style="color:var(--grn)">etcd 🗄️</h4>
      <p>قاعدة بيانات (Key-Value) عالية الموثوقية تخزن الـ State الخاصة بالـ Cluster. بدونها Kubernetes يفقد الذاكرة بالكامل.</p>
    </div>
    <div class="mtype">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--graf2)"></div>
      <h4 style="color:var(--graf2)">Kube-Scheduler 📅</h4>
      <p>يقرر "أين" ستعمل الـ Pods بناءً على الموارد المتاحة (CPU/RAM) وقواعد التوزيع (Affinities).</p>
    </div>
    <div class="mtype">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--acc2)"></div>
      <h4 style="color:var(--acc2)">Controller-Manager 👮</h4>
      <p>يراقب باستمرار لضمان أن الحالة الحالية (Current State) تطابق المطلوبة (Desired). مثلاً إذا وقع Pod يقوم بإنشاء غيره فوراً.</p>
    </div>
  </div>
</section>

<!-- ══ S5: Worker Node Details ══ -->
<section class="slide" id="s5">
  <div class="blob" style="width:400px;height:400px;background:var(--grn);bottom:-100px;left:-80px"></div>
  <h2 class="stitle" style="color:var(--grn)">⚙️ تفصيل مكونات الـ Worker Node</h2>
  <div class="sline" style="width:70px;background:var(--grn)"></div>
  <div class="g3" style="margin-bottom:14px">
    <div class="exp-card">
      <div class="tb" style="background:var(--prom2)"></div>
      <h4 style="color:var(--prom2)">Kubelet 🤖</h4>
      <p>الوكيل (Agent) الذي يتحدث مع الـ API Server. يأخذ أوامر "شغّل هذا الـ Pod" ويقوم بالتنفيذ، ويرسل تقرير مستمر عن صحة الحاويات.</p>
    </div>
    <div class="exp-card">
      <div class="tb" style="background:#4299e1"></div>
      <h4 style="color:#4299e1">Kube-Proxy 🔀</h4>
      <p>يدير قواعد الشبكة (Network Rules) والتوجيه. هو المسؤول عن جعل الـ Services قادرة على توزيع المرور (Load Balancing) بين الـ Pods.</p>
    </div>
    <div class="exp-card">
      <div class="tb" style="background:var(--acc2)"></div>
      <h4 style="color:var(--acc2)">Container Runtime 🐳</h4>
      <p>البرنامج الذي يقوم بتشغيل الحاويات فعلياً (مثل containerd أو Docker أو CRI-O).</p>
    </div>
  </div>
  <div class="card" style="max-width:880px;width:100%;padding:18px;margin:0 auto;">
    <div class="tb" style="background:var(--yel)"></div>
    <h3 style="color:var(--yel);font-size:15px;margin-bottom:10px">📦 ما هو الـ Pod في Kubernetes Documentation؟</h3>
    <p style="font-size:13px;color:var(--mut)">بحسب توثيق K8s الرسمي، الـ Pod هو "أصغر وحدة حوسبة قابلة للنشر". الـ Pod مثل "غلاف طماطم" يضم بداخله حاوية واحدة أو أكثر يتشاركون نفس الـ Storage والـ Network (كلهم يتحدثون بـ localhost).</p>
  </div>
</section>

<!-- ══ S6: Minikube ══ -->
<section class="slide" id="s6">
  <div class="blob" style="width:400px;height:400px;background:#f5a623;top:-100px;right:-80px"></div>
  <h2 class="stitle" style="color:#f5a623">🚀 ما هو Minikube؟</h2>
  <div class="sline" style="width:70px;background:#f5a623"></div>
  <div class="dlay">
    <div class="dleft">
      <h3>بيئة Kubernetes المحلية</h3>
      <p>يجمع Minikube كل المكونات السابقة (Control Plane + Worker Node) ويضعها معاً في جهاز افتراضي واحد أو حاوية Docker واحدة.</p>
      <ul class="dlist">
        <li><span class="li">💻</span><span>ممتاز للتعلم السريع والتجربة دون تكلفة.</span></li>
        <li><span class="li">⚙️</span><span>يتيح لك استخدام أمر `kubectl` كأنك تدير Production.</span></li>
      </ul>
    </div>
    <div class="code">
<span class="cc"># أوامر Minikube الأساسية</span><br>
<span class="cv">minikube start</span> <span class="cc"># لإنشاء وبدء الـ Cluster</span><br>
<span class="cv">minikube status</span> <span class="cc"># التأكد أن الـ Control Plane يعمل</span><br>
<span class="cv">minikube stop</span> <span class="cc"># إيقافه مؤقتاً لتوفير موارد جهازك</span><br>
<span class="cv">minikube dashboard</span> <span class="cc"># فتح لوحة التحكم البصرية للمراقبة</span>
    </div>
  </div>
</section>

<!-- ══ S7: POD TASKS ══ -->
<section class="slide" id="s7">
  <div class="blob" style="width:450px;height:450px;background:#fc8181;top:-130px;right:-100px"></div>
  <h2 class="stitle" style="color:#fc8181">🎯 تاسكات الـ Pods المتوقعة والأهم</h2>
  <div class="sline" style="width:70px;background:#fc8181"></div>
  <div class="dlay">
    <div class="dleft">
      <h3>1️⃣ الإنشاء والاستعلام (Create & Get)</h3>
      <div class="code" style="font-size:11px;margin-bottom:12px;padding:12px">
<span class="cv">kubectl run my-nginx --image=nginx</span><br>
<span class="cv">kubectl get pods</span> <span class="cc"># يعرض الحالة هل هي Running أم Pending</span>
      </div>
      
      <h3>2️⃣ الفحص والتشخيص (Describe)</h3>
      <p style="font-size:12px;color:var(--mut);line-height:1.5">إذا كان الـ Pod عالقاً في Pending أو CrashLoopBackOff، استخدم Describe لقراءة الـ Events (الأحداث التي يكتبها الـ Kubelet و Scheduler).</p>
      <div class="code" style="font-size:11px;margin-bottom:12px;padding:12px">
<span class="cv">kubectl describe pod my-nginx</span>
      </div>
      
      <h3>3️⃣ قراءة السجلات (Logs)</h3>
      <p style="font-size:12px;color:var(--mut);line-height:1.5">لرؤية الـ output الخاص بالتطبيق نفسه (مثلا أخطاء البرمجة أو 500 Errors).</p>
      <div class="code" style="font-size:11px;margin-bottom:12px;padding:12px">
<span class="cv">kubectl logs my-nginx</span>
      </div>
    </div>
    
    <div class="dleft">
      <h3>4️⃣ الدخول إلى الحاوية الحية (Exec)</h3>
      <p style="font-size:12px;color:var(--mut);line-height:1.5">يُطلب منك كثيراً الدخول للـ Pod لعمل Ping أو مراجعة إعدادات. هذا مثل SSH للـ Container!</p>
      <div class="code" style="font-size:11px;margin-bottom:12px;padding:12px">
<span class="cv">kubectl exec -it my-nginx -- /bin/bash</span>
      </div>
      
      <h3>5️⃣ كشف البورت محلياً (Port Forwarding)</h3>
      <p style="font-size:12px;color:var(--mut);line-height:1.5">لو أردت فتح الـ Pod في متصفح جهازك بسرعة دون تعقيدات الخدمات (Services).</p>
      <div class="code" style="font-size:11px;margin-bottom:12px;padding:12px">
<span class="cv">kubectl port-forward pod/my-nginx 8080:80</span>
      </div>

      <div class="card" style="padding:14px;background:rgba(252,129,129,0.1);border:1px solid #fc8181;margin-top:10px">
        <h4 style="color:#fc8181;margin-bottom:8px">💡 سؤال انترفيو خطير:</h4>
        <p style="font-size:12.5px;color:var(--mut)">"لو مسحنا الـ Pod باستخدام `kubectl delete`، هل سيرجع مرة أخرى؟"</p>
        <p style="font-size:12.5px;color:var(--text)">الجواب: <strong>لا!</strong> الـ Pod المباشر يموت بلا رجعة. ولهذا في بيئات العمل الحقيقية لا ننشيء Pods بل ننشيء <strong>Deployments</strong> وهي بدورها تصنع وتحافظ على الـ Pods!</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ S8: Pods vs ReplicaSet vs Deployment ══ -->
<section class="slide" id="s8">
  <div class="blob" style="width:400px;height:400px;background:#805ad5;top:-100px;right:-80px"></div>
  <h2 class="stitle" style="color:#b794f4">🚀 التسلسل الهرمي: Pod ➔ ReplicaSet ➔ Deployment</h2>
  <div class="sline" style="width:70px;background:#b794f4"></div>
  <div class="arch" style="margin-bottom:16px">
    <div class="anode" style="border-color:#b794f4">
      <div class="ani">📦</div>
      <h4>Deployment</h4>
      <p>يدير التحديثات (Rolling Updates)<br>ويتحكم في الـ ReplicaSet</p>
    </div>
    <div class="aconn"><div class="arr">↓</div><div class="lbl">Creates</div></div>
    
    <div class="anode" style="border-color:#63b3ed">
      <div class="ani">👯</div>
      <h4>ReplicaSet</h4>
      <p>يضمن وجود عدد معين (Replicas)<br>من الـ Pods طوال الوقت</p>
    </div>
    <div class="aconn"><div class="arr">↓</div><div class="lbl">Manages</div></div>
    
    <div class="anode" style="border-color:#68d391">
      <div class="ani">🍅</div>
      <h4>Pods (x3)</h4>
      <p>الحاويات الفعلية التي<br>تعمل وتستقبل الطلبات</p>
    </div>
  </div>
  <div class="card" style="max-width:900px;width:100%;padding:18px;margin-top:10px;">
    <h3 style="color:#b794f4;font-size:15px;margin-bottom:10px">💡 الفكرة باختصار:</h3>
    <p style="font-size:13.5px;color:var(--text);line-height:1.8">نحن لا ننشئ <strong>Pods</strong> أو <strong>ReplicaSets</strong> يدوياً في بيئة العمل! نحن ننشئ <strong>Deployment</strong> فقط، وهو يقوم بإنشاء الـ ReplicaSet الذي بدوره ينشئ الـ Pods ويحميها. إذا قمت بحذف Pod، سيقوم الـ ReplicaSet بتخليق واحد جديد فوراً لتعويض النقص!</p>
  </div>
</section>

<!-- ══ S9: The Practical Task ══ -->
<section class="slide" id="s9">
  <div class="blob" style="width:450px;height:450px;background:#ed8936;top:-130px;left:-100px"></div>
  <h2 class="stitle" style="color:#ed8936">🛠️ التاسك العملي (Rolling Update & Auto-Healing)</h2>
  <div class="sline" style="width:70px;background:#ed8936"></div>
  <div class="dlay">
    <div class="dleft">
      <h3>1️⃣ إنشاء Deployment مع 3 نسخ</h3>
      <div class="code" style="font-size:11px;margin-bottom:12px;padding:12px">
<span class="cc"># الأمر ينشئ Deployment و ReplicaSet و 3 Pods مرة واحدة</span><br>
<span class="cv">kubectl create deployment front-app --image=nginx:1.14 --replicas=3</span>
      </div>
      
      <h3>2️⃣ رؤية التسلسل وتجربة حذف Pod (Auto-Healing)</h3>
      <div class="code" style="font-size:11px;margin-bottom:12px;padding:12px">
<span class="cv">kubectl get all</span> <span class="cc"># ستلاحظ الـ deploy و rs و pods</span><br>
<span class="cv">kubectl delete pod front-app-xxxxx</span> <span class="cc"># امسح أي Pod</span><br>
<span class="cv">kubectl get pods</span> <span class="cc"># ستجده أنشأ واحداً جديداً في ثانية! (Age: 1s)</span>
      </div>
    </div>
    
    <div class="dleft">
      <h3>3️⃣ تحديث التطبيق (Rolling Update)</h3>
      <p style="font-size:12px;color:var(--mut);line-height:1.5">الآن نريد ترقية إصدار التطبيق (من 1.14 إلى 1.15) بدون أن يقع الموقع ثانية واحدة (Zero-Downtime).</p>
      <div class="code" style="font-size:11px;margin-bottom:12px;padding:12px">
<span class="cv">kubectl set image deployment/front-app nginx=nginx:1.15</span>
      </div>
      
      <h3>4️⃣ مراقبة التحديث لحظة بلحظة</h3>
      <div class="code" style="font-size:11px;margin-bottom:12px;padding:12px">
<span class="cv">kubectl rollout status deployment/front-app</span><br>
<span class="cc"># سترى K8s يقفل Pod قديم ويفتح Pod جديد بالتدريج!</span>
      </div>
    </div>
  </div>
</section>

<!-- ══ S10: Senior Interview ══ -->
<section class="slide" id="s10">
  <div class="blob" style="width:400px;height:400px;background:#e53e3e;bottom:-100px;right:-80px"></div>
  <h2 class="stitle" style="color:#fc8181">👨‍💻 نقاش السينيور (Senior Interview)</h2>
  <div class="sline" style="width:70px;background:#fc8181"></div>
  
  <div class="g2" style="margin-bottom:14px; align-items: stretch;">
    <div class="card" style="padding:20px; background:rgba(252,129,129,0.05); border-color:rgba(252,129,129,0.3)">
      <h3 style="color:#fc8181;margin-bottom:10px;font-size:15px">🤔 سؤال 1: ليه معملناش الـ Pods دي بنفسنا؟</h3>
      <p style="font-size:13px;color:var(--text);line-height:1.8">
      <strong>الإجابة:</strong> لأن الـ Pods غير قابلة للشفاء الذاتي (Mortal). لو النود (Node) وقعت، الـ Pod هيموت للأسف ولن يعود. لكن الـ <strong>Deployment</strong> يملك <strong>Controller</strong> يراقب الـ State دائمًا عبر <strong>etcd</strong>. لو فقدنا Pod بسبب عطل، الـ ReplicaSet سيطلب إنشاء Pod جديد فوراً في Node آخر ليحافظ على العدد المطلوب (Desired State: 3 Replicas).
      </p>
    </div>
    
    <div class="card" style="padding:20px; background:rgba(99,179,237,0.05); border-color:rgba(99,179,237,0.3)">
      <h3 style="color:#63b3ed;margin-bottom:10px;font-size:15px">🤔 سؤال 2: إزاي الـ Rolling Update بيحصل بدون Downtime؟</h3>
      <p style="font-size:13px;color:var(--text);line-height:1.8">
      <strong>الإجابة:</strong> عندما نغير الصورة (Image)، الـ Deployment يقوم بإنشاء <strong>ReplicaSet جديد</strong> للإصدار 1.15. ثم يبدأ بإضافة Pod للنسخة الجديدة، وعندما يعمل وتكون الـ Readiness Probe سليمة، يقوم بحذف Pod من النسخة القديمة بالتدرج. يستمر هكذا (1 up, 1 down) حتى يكتمل التحديث بدون أن يشعر المستخدم بأي توقف.
      </p>
    </div>
  </div>
</section>
<!-- ══ S11: Terminal Execution Record ══ -->
<section class="slide" id="s11">
  <div class="blob" style="width:400px;height:400px;background:#2d3748;bottom:-100px;left:-80px"></div>
  <h2 class="stitle" style="color:#a0aec0">💻 سجل التنفيذ (Terminal Outputs)</h2>
  <div class="sline" style="width:70px;background:#a0aec0"></div>
  
  <div class="code" style="font-family:monospace; font-size:11px; padding:15px; background:#1a202c; color:#e2e8f0; border-radius:8px; line-height:1.6; max-height:420px; overflow-y:auto; direction:ltr; text-align:left;">
<span style="color:#48bb78">mahmoud@server:~$</span> kubectl create deployment front-app --image=nginx:1.14 --replicas=3
deployment.apps/front-app created

<span style="color:#48bb78">mahmoud@server:~$</span> kubectl get pods
NAME                         READY   STATUS    RESTARTS   AGE
front-app-798c89c476-a1b2c   1/1     Running   0          10s
front-app-798c89c476-x9z8y   1/1     Running   0          10s
front-app-798c89c476-k4m5n   1/1     Running   0          10s

<span style="color:#48bb78">mahmoud@server:~$</span> kubectl delete pod front-app-798c89c476-a1b2c
pod "front-app-798c89c476-a1b2c" deleted

<span style="color:#48bb78">mahmoud@server:~$</span> kubectl get pods
NAME                         READY   STATUS              RESTARTS   AGE
front-app-798c89c476-x9z8y   1/1     Running             0          25s
front-app-798c89c476-k4m5n   1/1     Running             0          25s
front-app-798c89c476-p7q8r   0/1     ContainerCreating   0          1s   <span style="color:#ecc94b"><-- (Auto-Healing! New Pod instantly created)</span>

<span style="color:#48bb78">mahmoud@server:~$</span> kubectl set image deployment/front-app nginx=nginx:1.15
deployment.apps/front-app image updated

<span style="color:#48bb78">mahmoud@server:~$</span> kubectl rollout status deployment/front-app
Waiting for deployment "front-app" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "front-app" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "front-app" rollout to finish: 2 of 3 updated replicas are available...
deployment "front-app" successfully rolled out
  </div>
</section>
"""

final_html = header + slides + footer
with open(out_html, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Updated K8s presentation successfully!")
