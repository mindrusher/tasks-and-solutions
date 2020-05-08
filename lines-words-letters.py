text = '''Разнообразный и богатый опыт говорит нам, что высокое качество позиционных исследований позволяет выполнить важные задания по разработке форм воздействия. В частности, разбавленное изрядной долей эмпатии, рациональное мышление предполагает независимые способы реализации экономической целесообразности принимаемых решений. С учётом сложившейся международной обстановки, повышение уровня гражданского сознания предоставляет широкие возможности для системы обучения кадров, соответствующей насущным потребностям. Господа, курс на социально-ориентированный национальный проект способствует повышению качества позиций, занимаемых участниками в отношении поставленных задач.
Как уже неоднократно упомянуто, сделанные на базе интернет-аналитики выводы формируют глобальную экономическую сеть и при этом - указаны как претенденты на роль ключевых факторов. Учитывая ключевые сценарии поведения, семантический разбор внешних противодействий однозначно определяет каждого участника как способного принимать собственные решения касаемо системы массового участия.
С учётом сложившейся международной обстановки, реализация намеченных плановых заданий предоставляет широкие возможности для экспериментов, поражающих по своей масштабности и грандиозности. Как уже неоднократно упомянуто, тщательные исследования конкурентов и по сей день остаются уделом либералов, которые жаждут быть рассмотрены исключительно в разрезе маркетинговых и финансовых предпосылок. В частности, синтетическое тестирование создаёт необходимость включения в производственный план целого ряда внеочередных мероприятий с учётом комплекса соответствующих условий активизации. В целом, конечно, семантический разбор внешних противодействий выявляет срочную потребность первоочередных требований. Безусловно, современная методология разработки требует от нас анализа модели развития. Вот вам яркий пример современных тенденций - экономическая повестка сегодняшнего дня не даёт нам иного выбора, кроме определения стандартных подходов.'''

lines = 0
words = 0
letters = 0
 
for line in text:
    lines += 1
    letters += len(line)
    pos = 'out'
 
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
 
print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)