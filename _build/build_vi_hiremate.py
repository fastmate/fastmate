# Vietnamese page for HireMate (the extension's own UI stays English). Executed by build_vi.py.
HM_CHECKOUT = 'https://fastmate.lemonsqueezy.com/checkout/buy/b649a58d-00c4-41a0-ad82-a3b9c0660f90'

page('vi/hiremate/index.html', 'HireMate — Lưu hồ sơ LinkedIn™ ra Excel và quản lý nguồn ứng viên',
 'HireMate là tiện ích Chrome cho nhân sự tuyển dụng: lưu hồ sơ ứng viên đang xem thành danh sách Excel gọn gàng, quản lý nguồn ứng viên với dashboard, bản đồ nhân tài và quy trình tuyển dụng.',
f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">HireMate · Tiện ích Chrome</span>
      <h1>Lập danh sách ứng viên trong vài phút, không phải vài giờ.</h1>
      <p class="lead">HireMate là bảng bên (side panel) trên Chrome dành cho nhân sự tuyển dụng. Mở hồ sơ ứng viên, lưu bằng một cú bấm và xuất file Excel gọn gàng với đầy đủ vị trí, công ty, ngành, học vấn — rồi quản lý toàn bộ nguồn ứng viên trong một dashboard.</p>
      <div class="actions">
        <a class="btn btn-primary" href="#">Thêm vào Chrome — miễn phí</a>
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
      <span class="eyebrow">Tính năng</span>
      <h2>Mọi việc sau khi “đã tìm được ứng viên tốt”</h2>
      <p class="lead">Thôi sao chép, dán thủ công. Dành thời gian để trò chuyện với ứng viên.</p>
    </div>
    <div class="grid-3">
      <div class="card"><div class="icon">{ICON['table']}</div><h3>Một cú bấm ra Excel</h3><p>Mọi vị trí, thời gian, công ty, ngành, mô tả công việc và trường học — chia cột đánh số, sẵn sàng lọc trong Excel.</p></div>
      <div class="card"><div class="icon green">{ICON['search']}</div><h3>Tìm kiếm &amp; chọn lọc</h3><p>Tìm người theo chức danh, địa điểm, công ty, ngành; xem ngay vị trí hiện tại và tổng số năm kinh nghiệm, lưu người phù hợp.</p></div>
      <div class="card"><div class="icon">{ICON['chart']}</div><h3>Bản đồ nhân tài</h3><p>Ứng viên đang làm ở đâu, thuộc ngành nào, học trường gì, bao nhiêu năm kinh nghiệm — bức tranh để mang vào mỗi buổi trao đổi với quản lý tuyển dụng.</p></div>
      <div class="card"><div class="icon green">{ICON['trend']}</div><h3>Ai có khả năng chuyển việc</h3><p>Ước tính minh bạch ai có thể đổi việc trong vài tháng tới, dựa trên quy luật sự nghiệp trong chính danh sách bạn đã lưu — kèm lý do.</p></div>
      <div class="card"><div class="icon">{ICON['board']}</div><h3>Quy trình tuyển dụng</h3><p>Mỗi vị trí một bảng: kéo thả ứng viên từ Tìm nguồn đến Trúng tuyển, thêm ghi chú, thẻ và theo dõi phễu tuyển dụng.</p></div>
      <div class="card"><div class="icon green">{ICON['refresh']}</div><h3>Luôn cập nhật</h3><p>Làm mới hồ sơ đã lưu để lấy vị trí mới và được báo khi ứng viên đổi công ty.</p></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head"><h2>Dùng thế nào</h2></div>
    <div class="grid-3 steps">
      <div class="step"><h3>Cài và mở</h3><p class="muted">Thêm HireMate vào Chrome và ghim lên thanh công cụ. Bấm biểu tượng để mở bảng bên.</p></div>
      <div class="step"><h3>Xem và lưu</h3><p class="muted">Mở hồ sơ ứng viên — HireMate tự đọc giúp bạn. Chỉnh sửa nếu cần, rồi lưu vào danh sách.</p></div>
      <div class="step"><h3>Xuất và hành động</h3><p class="muted">Xuất ra Excel, hoặc dùng dashboard để xem bản đồ nhân tài, theo dõi quy trình và tìm người có thể sẵn sàng chuyển việc.</p></div>
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
          <li>Lưu hồ sơ từ bảng bên &amp; xuất Excel</li>
          <li>Dashboard, bản đồ nhân tài, ghi chú &amp; thẻ</li>
          <li>Tìm kiếm: lấy 10 hồ sơ mỗi lượt, tối đa 50 mỗi ngày</li>
          <li>Tối đa 3 dự án</li>
          <li>“Có khả năng chuyển việc nhất”: xem trước 3 người đầu</li>
        </ul>
        <a class="btn btn-ghost" href="#">Thêm vào Chrome</a>
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
      <details><summary>Bản miễn phí có gì?</summary><p>Lưu hồ sơ, xuất Excel, dashboard và bản đồ nhân tài đều miễn phí. Bản miễn phí cho lấy 10 kết quả tìm kiếm mỗi lượt và tối đa 50 mỗi ngày, tối đa 3 dự án và xem trước 3 người có khả năng chuyển việc nhất. Premium bỏ các giới hạn này và thêm vị trí, công ty hiện tại, tổng kinh nghiệm vào kết quả tìm kiếm.</p></details>
      <details><summary>Có thể hủy Premium không?</summary><p>Có, bất cứ lúc nào qua đường link trong email biên nhận. Bạn vẫn dùng Premium đến hết kỳ đã thanh toán. Xem <a href="{{P}}vi/refund.html">Chính sách hoàn tiền</a>.</p></details>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta">
      <div><h2>Lập danh sách ứng viên tiếp theo trong vài phút.</h2><p>Cài miễn phí. Không cần tạo tài khoản.</p></div>
      <a class="btn btn-ghost" href="#">Thêm HireMate vào Chrome</a>
    </div>
  </div>
</section>''', lang='vi', alt='hiremate/index.html')
