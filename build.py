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
  <div class="snote">
    <div class="st">⚠️ تنبيه هام</div>
    <div class="bilang">
      <div class="ar"><span class="arlabel">🇪🇬 ملاحظة</span>لا تعمل تطبيقات المستخدم أبداً على الـ Control Plane، بل يتم توجيهها لتعمل على الـ Worker Nodes لضمان استقرار النظام.</div>
    </div>
  </div>
</section>

<!-- ══ S3: Control Plane ══ -->
<section class="slide" id="s3">
  <div class="blob" style="width:400px;height:400px;background:var(--acc2);top:-100px;right:-80px"></div>
  <h2 class="stitle">🧠 مكونات الـ Control Plane</h2>
  <div class="sline" style="width:70px;background:var(--acc2)"></div>
  <div class="g4" style="margin-bottom:14px">
    <div class="mtype">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--acc)"></div>
      <h4 style="color:var(--acc)">Kube-API Server 🚪</h4>
      <p>واجهة التخاطب الأساسية مع K8s. أي أمر تكتبه (مثل kubectl) يمر عبره أولاً.</p>
    </div>
    <div class="mtype">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--grn)"></div>
      <h4 style="color:var(--grn)">etcd 🗄️</h4>
      <p>قاعدة البيانات عالية الموثوقية التي تخزن كل ما يخص الـ Cluster وحالته.</p>
    </div>
    <div class="mtype">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--graf2)"></div>
      <h4 style="color:var(--graf2)">Kube-Scheduler 📅</h4>
      <p>المكون المسؤول عن اختيار الـ Node المناسبة لتشغيل الـ Pod الجديد بناءً على الموارد.</p>
    </div>
    <div class="mtype">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--acc2)"></div>
      <h4 style="color:var(--acc2)">Controller-Manager 👮</h4>
      <p>يراقب النظام باستمرار لضمان أن الحالة الحالية تطابق الحالة المطلوبة (Desired State).</p>
    </div>
  </div>
</section>

<!-- ══ S4: Worker Node ══ -->
<section class="slide" id="s4">
  <div class="blob" style="width:400px;height:400px;background:var(--grn);bottom:-100px;left:-80px"></div>
  <h2 class="stitle" style="color:var(--grn)">⚙️ مكونات الـ Worker Node</h2>
  <div class="sline" style="width:70px;background:var(--grn)"></div>
  <div class="g3" style="margin-bottom:14px">
    <div class="exp-card">
      <div class="tb" style="background:var(--prom2)"></div>
      <h4 style="color:var(--prom2)">Kubelet 🤖</h4>
      <p>الوكيل (Agent) الذي يعمل على كل Node ويتأكد من تشغيل الحاويات كما هو مطلوب من قبل الـ Control Plane.</p>
    </div>
    <div class="exp-card">
      <div class="tb" style="background:#4299e1"></div>
      <h4 style="color:#4299e1">Kube-Proxy 🔀</h4>
      <p>يدير قواعد الشبكة (Network Rules) للسماح بالاتصال بين التطبيقات داخل وخارج الـ Cluster.</p>
    </div>
    <div class="exp-card">
      <div class="tb" style="background:var(--acc2)"></div>
      <h4 style="color:var(--acc2)">Container Runtime 🐳</h4>
      <p>البرنامج الذي يقوم بتشغيل الحاويات فعلياً (مثل Docker أو containerd).</p>
    </div>
  </div>
  <div class="card" style="max-width:880px;width:100%;padding:18px;margin:0 auto;">
    <div class="tb" style="background:var(--yel)"></div>
    <h3 style="color:var(--yel);font-size:15px;margin-bottom:10px">📦 ما هو الـ Pod؟</h3>
    <p style="font-size:13px;color:var(--mut)">أصغر وحدة قابلة للنشر في Kubernetes. يمكن أن يحتوي على حاوية واحدة أو أكثر تعمل معاً ككيان واحد وتتشارك نفس موارد الشبكة والمساحة.</p>
  </div>
</section>

<!-- ══ S5: Minikube ══ -->
<section class="slide" id="s5">
  <div class="blob" style="width:400px;height:400px;background:#f5a623;top:-100px;right:-80px"></div>
  <h2 class="stitle" style="color:#f5a623">🚀 ما هو Minikube ولماذا نستخدمه؟</h2>
  <div class="sline" style="width:70px;background:#f5a623"></div>
  <div class="dlay">
    <div class="dleft">
      <h3>بيئة Kubernetes المحلية</h3>
      <p>تشغيل K8s كامل يحتاج إلى موارد ضخمة وسيرفرات معقدة. Minikube يوفر لك Cluster مبسط على جهازك.</p>
      <ul class="dlist">
        <li><span class="li">💻</span><span>يعمل محلياً على جهازك الشخصي</span></li>
        <li><span class="li">📦</span><span>يحتوي على Control Plane و Worker Node في بيئة واحدة</span></li>
        <li><span class="li">🧪</span><span>مثالي للتدريب وتطوير واختبار التطبيقات قبل النشر</span></li>
        <li><span class="li">⚡</span><span>خفيف الاستهلاك مقارنة بعنقود K8s حقيقي</span></li>
      </ul>
    </div>
    <div class="card" style="padding:20px">
      <div class="tb" style="background:var(--acc)"></div>
      <h3 style="color:var(--acc);margin-bottom:14px;font-size:14px">💡 كيف يعمل Minikube؟</h3>
      <p style="font-size:13px;color:var(--text);line-height:1.8">
        Minikube يقوم بإنشاء جهاز افتراضي (VM) أو حاوية Docker (Container) ويقوم بتثبيت وإعداد Kubernetes بداخلها (Single-Node Cluster).
        <br><br>
        بذلك يمكنك استخدام أوامر <code>kubectl</code> من جهازك للتحكم في هذا العنقود المصغر تماماً كما لو كان بيئة عمل حقيقية (Production).
      </p>
    </div>
  </div>
</section>

<!-- ══ S6: First Task ══ -->
<section class="slide" id="s6">
  <div class="blob" style="width:400px;height:400px;background:#68d391;top:-100px;left:-80px"></div>
  <h2 class="stitle" style="color:#68d391">🎯 توقعات "أول تاسك"</h2>
  <div class="sline" style="width:70px;background:#68d391"></div>
  <div class="dlay">
    <div class="dleft">
      <h3>الخطوات العملية المتوقعة</h3>
      <p>الهدف سيكون إعداد بيئة العمل (Minikube) وتشغيل أول تطبيق لك عليها (مثلاً موقع Nginx).</p>
      <div class="code" style="font-size:11.5px;margin-bottom:12px">
<span class="cc"># 1. بدء تشغيل العنقود المحلي</span><br>
<span class="cv">minikube start</span><br><br>
<span class="cc"># 2. إنشاء ونشر تطبيق بسيط (Deployment)</span><br>
<span class="cv">kubectl create deployment hello-minikube --image=nginx</span><br><br>
<span class="cc"># 3. كشف التطبيق للشبكة الخارجية (Expose)</span><br>
<span class="cv">kubectl expose deployment hello-minikube --type=NodePort --port=80</span><br><br>
<span class="cc"># 4. فتح التطبيق في المتصفح</span><br>
<span class="cv">minikube service hello-minikube</span>
      </div>
    </div>
    <div>
      <div class="card" style="padding:14px;background:rgba(104,211,145,0.1);border:1px solid #68d391;margin-top:10px">
        <h4 style="color:#68d391;margin-bottom:8px">💡 نصيحة:</h4>
        <p style="font-size:13.5px;color:var(--text)">توقع أن تواجه بعض التحديات في التثبيت لأول مرة (مثل صلاحيات الشبكة أو استهلاك الرامات)، ولكنها جزء من مرحلة التعلم الأساسية في لينكس والـ DevOps!</p>
      </div>
    </div>
  </div>
</section>
"""

final_html = header + slides + footer
with open(out_html, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Created K8s presentation successfully!")
