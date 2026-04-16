function updateFlex(property, value, btn) {
    const container = document.getElementById('container');

    // CSS 적용
    container.style[property] = value;

    // 코드 텍스트 업데이트
    const textId = {
        'flexDirection': 'css-direction',
        'justifyContent': 'css-justify',
        'alignItems': 'css-align',
        'flexWrap': 'css-wrap'
    }[property];

    const targetEl = document.getElementById(textId);
    if (targetEl) {
        targetEl.innerText = value;
        targetEl.classList.remove('animate-pulse');
        void targetEl.offsetWidth; // Restart animation
        targetEl.classList.add('text-white', 'duration-500');
        setTimeout(() => targetEl.classList.remove('text-white'), 500);
    }

    // 버튼 활성화 스타일 및 그룹 하이라이트
    const group = btn.closest('.control-group');
    document.querySelectorAll('.control-group').forEach(g => g.classList.remove('ring-2', 'ring-indigo-500/20', 'bg-white'));
    group.classList.add('ring-2', 'ring-indigo-500/20', 'bg-white');

    const buttons = btn.parentElement.querySelectorAll('button');
    buttons.forEach(b => b.classList.remove('btn-active'));
    btn.classList.add('btn-active');

    // 컨테이너에 피드백 효과
    container.classList.add('ring-4', 'ring-indigo-500/10');
    setTimeout(() => container.classList.remove('ring-4', 'ring-indigo-500/10'), 400);
}
