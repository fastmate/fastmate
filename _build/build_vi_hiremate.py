# Vietnamese page for HireMate (the extension's own UI stays English). Executed by build_vi.py.
HM_CHECKOUT = 'https://fastmate.lemonsqueezy.com/checkout/buy/b649a58d-00c4-41a0-ad82-a3b9c0660f90'

page('vi/hiremate/index.html', 'HireMate — Xuất hồ sơ LinkedIn™ ra Excel, biết ai sắp chuyển việc, xem lộ trình nghề nghiệp',
 'HireMate là tiện ích Chrome cho nhân sự tuyển dụng: xuất hồ sơ LinkedIn™ ra Excel bằng một cú bấm, biết ứng viên nào có khả năng chuyển việc và so sánh lộ trình nghề nghiệp của bất kỳ vị trí nào.',
f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">HireMate · Tiện ích Chrome</span>
      <h1>Xuất Excel một cú bấm. Biết ai sắp chuyển việc. Thấy rõ lộ trình nghề.</h1>
      <p class="lead">HireMate là bảng bên (side panel) trên Chrome dành cho nhân sự tuyển dụng: lưu hồ sơ LinkedIn™ ra file Excel gọn gàng bằng một cú bấm, biết ứng viên nào có khả năng chuyển việc, và so sánh lộ trình nghề nghiệp thực tế của bất kỳ vị trí nào — dữ liệu không rời khỏi trình duyệt.</p>
      <div class="actions">
        <a class="btn btn-primary" href="https://chromewebstore.google.com/detail/fmhkmikhenpkemjmddogaildfdnhddfe?utm_source=fastmate.io.vn" target="_blank" rel="noopener">Thêm vào Chrome — miễn phí</a>
        <a class="btn btn-ghost" href="#bang-gia">Xem bảng giá</a>
      </div>
      <div class="trust"><span>Dữ liệu chỉ lưu trong trình duyệt</span><span>Không cần tạo tài khoản</span><span>Dùng tài khoản LinkedIn của chính bạn</span><span>Giao diện tiếng Anh</span></div>
    </div>
    <div class="hero-art"><img src="{{P}}assets/hiremate-hero.jpg" alt="HireMate — từ hồ sơ ra Excel"></div>
  </div>
</section>

<section id="tinh-nang">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Ba tính năng chính</span>
      <h2>Ba việc HireMate làm giúp bạn</h2>
      <p class="lead">Tiết kiệm thời gian với từng hồ sơ, biết nên gọi ai trước, và thống nhất yêu cầu thực tế với quản lý tuyển dụng.</p>
    </div>
    <div class="features">
      <div class="feature-row">
        <div class="feature-text">
          <div class="feature-tag"><span class="feature-num">1</span><span class="eyebrow">Xuất Excel một cú bấm</span></div>
          <h3>Hồ sơ nào cũng ra Excel chỉ với một cú bấm</h3>
          <p>Mở hồ sơ LinkedIn™ của ứng viên, HireMate tự đọc mọi vị trí, thời gian, công ty, ngành, mô tả công việc và trường học. Lưu bằng một cú bấm (Alt+S) và xuất file Excel gọn gàng — mỗi ứng viên một dòng, cột đánh số sẵn sàng để lọc.</p>
          <ul class="ticks"><li>Chỉnh sửa mọi trường trước khi lưu</li><li>Tìm người theo chức danh, địa điểm, công ty và ngành</li><li>Xuất toàn bộ, theo bộ lọc hoặc chỉ những dòng bạn chọn</li></ul>
        </div>
        <div class="feature-shot"><img src="{{P}}assets/hiremate-export.jpg" alt="Bảng ứng viên của HireMate với nút Export to Excel" width="752" height="692" loading="lazy"></div>
      </div>
      <div class="feature-row flip">
        <div class="feature-text">
          <div class="feature-tag"><span class="feature-num">2</span><span class="eyebrow">Ai sắp chuyển việc</span></div>
          <h3>Biết ai có khả năng chuyển việc</h3>
          <p>HireMate chấm mỗi ứng viên đã lưu mức Cao, Trung bình hoặc Thấp về khả năng đổi việc trong vài tháng tới — luôn kèm lý do, để bạn biết nên liên hệ ai trước.</p>
          <ul class="ticks"><li>Thời gian ở vị trí hiện tại so với quy luật của chính họ</li><li>Bao lâu chưa được thăng chức, người ta thường ở công ty đó bao lâu</li><li>Báo ngay khi ứng viên đổi việc lúc làm mới hồ sơ</li></ul>
        </div>
        <div class="feature-shot"><img src="{{P}}assets/hiremate-move.jpg" alt="Danh sách ứng viên có khả năng chuyển việc nhất kèm lý do" width="752" height="692" loading="lazy"></div>
      </div>
      <div class="feature-row">
        <div class="feature-text">
          <div class="feature-tag"><span class="feature-num">3</span><span class="eyebrow">Lộ trình nghề nghiệp</span></div>
          <h3>So sánh lộ trình nghề nghiệp của bất kỳ vị trí nào</h3>
          <p>Quét thị trường cho một nhóm nghề ở quốc gia hoặc thành phố bạn tuyển và xem toàn bộ nấc thang từ thực tập đến C-level: người ta lên mỗi cấp khi có bao nhiêu năm kinh nghiệm, ở lại bao lâu và ai được lên tiếp.</p>
          <ul class="ticks"><li>Nhận định sẵn cho buổi trao đổi với quản lý — ví dụ “Yêu cầu 6–9 năm, đừng đòi 10+”</li><li>Ở mỗi cấp: ai lên tiếp, ai ở lại, ai rời nghề</li><li>So sánh bất kỳ ứng viên nào với thị trường — 20 nhóm nghề, đọc chức danh 9 ngôn ngữ</li></ul>
        </div>
        <div class="feature-shot"><img src="{{P}}assets/hiremate-career.jpg" alt="Nấc thang nghề nghiệp của HireMate kèm nhận định và ứng viên được so sánh" width="752" height="692" loading="lazy"></div>
      </div>
    </div>
    <h3 class="also-title">Và còn có</h3>
    <div class="grid-3">
      <div class="card"><div class="icon">{ICON['search']}</div><h3>Tìm kiếm &amp; chọn lọc</h3><p>Tìm người theo chức danh, địa điểm, công ty, ngành; xem ngay vị trí hiện tại và tổng số năm kinh nghiệm, lưu người phù hợp.</p></div>
      <div class="card"><div class="icon green">{ICON['chart']}</div><h3>Bản đồ nhân tài</h3><p>Ứng viên đã lưu đang làm ở đâu, thuộc ngành nào, học trường gì, bao nhiêu năm kinh nghiệm.</p></div>
      <div class="card"><div class="icon">{ICON['board']}</div><h3>Quy trình tuyển dụng</h3><p>Mỗi vị trí một bảng: kéo thả ứng viên từ Tìm nguồn đến Trúng tuyển, thêm ghi chú, thẻ và theo dõi phễu tuyển dụng.</p></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head"><h2>Dùng thế nào</h2></div>
    <div class="grid-3 steps">
      <div class="step"><h3>Cài và mở</h3><p class="muted">Thêm HireMate vào Chrome và ghim lên thanh công cụ. Bấm biểu tượng để mở bảng bên.</p></div>
      <div class="step"><h3>Xem và lưu</h3><p class="muted">Mở hồ sơ ứng viên — HireMate tự đọc giúp bạn. Chỉnh sửa nếu cần, rồi lưu vào danh sách.</p></div>
      <div class="step"><h3>Xuất và hành động</h3><p class="muted">Xuất ra Excel, liên hệ trước với người có khả năng chuyển việc cao, và dùng lộ trình nghề nghiệp để thống nhất yêu cầu thực tế với quản lý tuyển dụng.</p></div>
    </div>
  </div>
</section>

<section id="bang-gia">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Bảng giá</span>
      <h2>Bắt đầu miễn phí. Nâng cấp khi giúp bạn tiết kiệm hàng giờ.</h2>
    </div>
    <div class="billing" role="group" aria-label="Kỳ thanh toán">
      <button type="button" data-period="monthly" class="active">Theo tháng</button>
      <button type="button" data-period="quarterly">Theo quý <span class="save">−20%</span></button>
      <button type="button" data-period="yearly">Theo năm <span class="save">−30%</span></button>
    </div>
    <div class="pricing">
      <div class="plan">
        <div><h3>Miễn phí</h3><p class="muted" style="margin:0">Cho nhu cầu tìm nguồn thỉnh thoảng</p></div>
        <div class="price">$0<small> mãi mãi</small></div>
        <ul>
          <li>Lưu hồ sơ &amp; xuất Excel bằng một cú bấm</li>
          <li>“Có khả năng chuyển việc nhất”: xem trước 3 người đầu</li>
          <li>Nấc thang nghề nghiệp từ ứng viên đã lưu</li>
          <li>Tìm kiếm: lấy 10 hồ sơ mỗi lượt, tối đa 50 mỗi ngày</li>
          <li>Dashboard, bản đồ nhân tài, ghi chú &amp; thẻ, tối đa 3 dự án</li>
        </ul>
        <a class="btn btn-ghost" href="https://chromewebstore.google.com/detail/fmhkmikhenpkemjmddogaildfdnhddfe?utm_source=fastmate.io.vn" target="_blank" rel="noopener">Thêm vào Chrome</a>
      </div>
      <div class="plan featured">
        <div><h3>Premium</h3><p class="muted" style="margin:0">Cho người tìm nguồn mỗi ngày</p></div>
        <div>
          <div class="price"><span id="pPrice">$4.99</span><small> / tháng</small></div>
          <div class="muted" id="pBilled" style="font-size:14px;margin-top:6px">Thanh toán hằng tháng</div>
        </div>
        <ul>
          <li>Mọi tính năng miễn phí</li>
          <li><strong>Đầy đủ danh sách “Có khả năng chuyển việc”</strong> kèm lý do</li>
          <li><strong>Quét thị trường cho lộ trình nghề nghiệp</strong> — nhận định, ai được lên tiếp và so sánh ứng viên</li>
          <li><strong>Lấy hồ sơ từ tìm kiếm không giới hạn</strong> — không giới hạn theo ngày, 50 hồ sơ mỗi lượt</li>
          <li><strong>Vị trí, công ty hiện tại &amp; tổng kinh nghiệm</strong> ngay trong kết quả tìm kiếm</li>
          <li><strong>Không giới hạn dự án</strong></li>
        </ul>
        <a class="btn btn-green" href="{HM_CHECKOUT}" target="_blank" rel="noopener">Mua Premium</a>
      </div>
    </div>
    <p class="billing-note muted">Giá tính bằng USD, thanh toán bằng thẻ; có thể phát sinh thuế. Hủy bất cứ lúc nào. Thanh toán an toàn qua Lemon Squeezy.</p>
  </div>
</section>
<script>
  // $4.99/tháng; theo quý −20% ($11.98 mỗi 3 tháng); theo năm −30% ($41.92 mỗi năm).
  (function () {{
    var plans = {{
      monthly: {{ price: '$4.99', billed: 'Thanh toán hằng tháng' }},
      quarterly: {{ price: '$3.99', billed: '$11.98 mỗi 3 tháng — tiết kiệm 20%' }},
      yearly: {{ price: '$3.49', billed: '$41.92 mỗi năm — tiết kiệm 30%' }}
    }};
    var buttons = document.querySelectorAll('.billing button');
    buttons.forEach(function (b) {{
      b.addEventListener('click', function () {{
        buttons.forEach(function (x) {{ x.classList.toggle('active', x === b); }});
        var p = plans[b.dataset.period];
        document.getElementById('pPrice').textContent = p.price;
        document.getElementById('pBilled').textContent = p.billed;
      }});
    }});
  }})();
</script>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head"><h2>Câu hỏi thường gặp</h2></div>
    <div class="faq">
      <details><summary>Dữ liệu ứng viên được lưu ở đâu?</summary><p>Chỉ trong trình duyệt của bạn (bộ nhớ của tiện ích Chrome). HireMate không có máy chủ nhận dữ liệu ứng viên. Bạn có thể sao lưu hoặc xóa toàn bộ bất cứ lúc nào trong dashboard.</p></details>
      <details><summary>Có cần tài khoản LinkedIn Recruiter không?</summary><p>Không. HireMate làm việc với những hồ sơ bạn vẫn xem được bằng tài khoản LinkedIn của mình. Tài khoản LinkedIn miễn phí có giới hạn tìm kiếm riêng, và HireMate tuân thủ giới hạn đó.</p></details>
      <details><summary>HireMate có gửi tin nhắn hay lời mời kết nối không?</summary><p>Không. HireMate không bao giờ gửi tin nhắn, lời mời hay bài đăng thay bạn. Các tính năng hàng loạt đều có giới hạn và giãn cách để bảo vệ tài khoản của bạn.</p></details>
      <details><summary>“Có khả năng chuyển việc” được tính thế nào?</summary><p>Từ quy luật sự nghiệp trong chính danh sách bạn đã lưu: người ta thường ở bao lâu trước khi chuyển, người này thường ở mỗi công ty bao lâu, bao lâu chưa được thăng chức và các tín hiệu tương tự. Đây là ước tính kèm lý do — không phải sự thật về bất kỳ ai.</p></details>
      <details><summary>Lộ trình nghề nghiệp hoạt động thế nào?</summary><p>Chọn nhóm nghề, địa điểm và (tùy chọn) ngành. HireMate tìm trên LinkedIn bằng phiên đăng nhập của chính bạn, đọc tối đa 50 hồ sơ mỗi lượt với tốc độ như người thật và xếp từng vị trí lên nấc thang 8 cấp từ thực tập đến C-level; ứng viên bạn đã lưu cũng được tính vào. Quét thêm để mở rộng dữ liệu — người đã có sẽ được bỏ qua.</p></details>
      <details><summary>Quét thị trường lưu những gì?</summary><p>Chỉ dữ liệu nghề nghiệp ẩn danh: chức danh được xếp vào nhóm nghề và cấp bậc, kèm thời gian. Không lưu tên, ảnh hay link hồ sơ, người được quét không bị thêm vào danh sách ứng viên, và mọi thứ chỉ nằm trong trình duyệt của bạn.</p></details>
      <details><summary>Bản miễn phí có gì?</summary><p>Lưu hồ sơ và xuất Excel một cú bấm, dashboard, bản đồ nhân tài và nấc thang nghề nghiệp từ ứng viên đã lưu đều miễn phí. Bản miễn phí cho lấy 10 kết quả tìm kiếm mỗi lượt và tối đa 50 mỗi ngày, tối đa 3 dự án và xem trước 3 người có khả năng chuyển việc nhất. Premium bỏ các giới hạn này, thêm quét thị trường cho lộ trình nghề nghiệp kèm nhận định, cùng vị trí, công ty hiện tại và tổng kinh nghiệm trong kết quả tìm kiếm.</p></details>
      <details><summary>Có thể hủy Premium không?</summary><p>Có, bất cứ lúc nào qua đường link trong email biên nhận. Bạn vẫn dùng Premium đến hết kỳ đã thanh toán. Xem <a href="{{P}}vi/refund.html">Chính sách hoàn tiền</a>.</p></details>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta">
      <div><h2>Xuất Excel, ưu tiên đúng người, so sánh với thị trường — trong một bảng bên.</h2><p>Cài miễn phí. Không cần tạo tài khoản.</p></div>
      <a class="btn btn-ghost" href="https://chromewebstore.google.com/detail/fmhkmikhenpkemjmddogaildfdnhddfe?utm_source=fastmate.io.vn" target="_blank" rel="noopener">Thêm HireMate vào Chrome</a>
    </div>
  </div>
</section>''', lang='vi', alt='hiremate/index.html')
